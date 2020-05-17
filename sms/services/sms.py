import requests
from django.utils.timezone import datetime
from sms.models import Message, SmsInfo
from django.conf import settings
import africastalking

# Initialize SDK
from sms.services.contacts import get_all_contacts_numbers, return_contact_numbers_with_tag, get_contact_number

username = settings.AFRICASTALKING_USERNAME
apikey = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, apikey)
sms = africastalking.SMS


def send_sms(message, recipients):
    """
    Send sms
    """
    recipients = recipients
    message = message
    time_sent = datetime.now()
    try:
        # buy a Dedicated Short Code to get a sender ID
        # response = sms.send(message, recipients, sender)
        response = sms.send(message, recipients)

        print(response)

        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=response['SMSMessageData']['Message'],
            success=True)
        sms_info_obj.save()

        # save the messages sent
        message_obj_list = []
        for i in response['SMSMessageData']['Recipients']:
            message_obj_list.append(
                Message(
                    message_info=sms_info_obj,
                    message_id=i["messageId"],
                    number=i["number"],
                    cost=i["cost"],
                    status_code=i["statusCode"], ))

        # save the list objects into the database in one query
        Message.objects.bulk_create(message_obj_list)

    except requests.exceptions.ConnectionError:
        raise Exception("Network Error")
    except requests.HTTPError:
        raise Exception("Network Error")
    except Exception as e:
        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=e,
            success=False)
        sms_info_obj.save()
        raise e
    else:
        return response


def send_to_all_contacts(message):
    # send message to all contacts
    try:
        send_sms(message, get_all_contacts_numbers())
    except Exception as e:
        raise e


def send_to_tags(message, tags):
    # send message to specific tags
    try:
        send_sms(message, return_contact_numbers_with_tag(tags))
    except Exception as e:
        raise e


def send_to_contact(message, contact):
    # send message to specific contact
    try:
        send_sms(message, get_contact_number(contact))
    except Exception as e:
        raise e
