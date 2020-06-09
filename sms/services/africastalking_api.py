from datetime import datetime

import africastalking
import requests
from django.conf import settings

from contacts.models import Contact
from sms.models import SmsInfo, Message

# Initialize SDK
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(user, message, recipients):
    """
    Send sms
    """
    recipients = recipients
    message = message
    time_sent = datetime.now()
    #
    if len(message) > 160:
        raise Exception("Ensure your message has less that 160 characters")

    try:
        # buy a Dedicated Short Code to get a sender ID
        # response = sms.send(message, recipients, sender)
        response = sms.send(message, recipients)

        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=response['SMSMessageData']['Message'],
            user=user,
            success=True)
        sms_info_obj.save()

        # save the messages sent
        contact_list = Contact.objects.all()
        message_obj_list = []

        for i in response['SMSMessageData']['Recipients']:
            # check for contact
            if contact_list.filter(phone_number__exact=i["number"]).exists:
                # if we have the contact saved...
                message_obj_list.append(
                    Message(
                        message_info=sms_info_obj,
                        message_id=i["messageId"],
                        contact=contact_list.get(phone_number__exact=i["number"]),
                        cost=i["cost"],
                        status_code=i["statusCode"],
                        number=i["number"]
                    ))
            else:
                # create & save contact
                contact_obj = Contact(
                    first_name="First Name",
                    last_name="Doe",
                    phone_number=i["number"])
                contact_obj.save()
                #
                #
                # save message
                message_obj_list.append(
                    Message(
                        message_info=sms_info_obj,
                        message_id=i["messageId"],
                        contact=contact_obj,
                        cost=i["cost"],
                        number=i["number"],
                        status_code=i["statusCode"], ))

        # save the list objects into the database in one query
        Message.objects.bulk_create(message_obj_list)

    except requests.exceptions.ConnectionError as e:
        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=e,
            user=user,
            success=False)
        sms_info_obj.save()
        raise Exception("Network Connection Error")
    except requests.HTTPError as e:
        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=e,
            user=user,
            success=False)
        sms_info_obj.save()
        raise Exception("HTTP Network Error")
    except Exception as e:
        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=e,
            user=user,
            success=False)
        sms_info_obj.save()
        raise e
    else:
        return response
