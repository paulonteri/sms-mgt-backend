from django.utils.timezone import datetime
from sms.models import Message, SmsInfo
from django.conf import settings
import africastalking


# Initialize SDK
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
                    status_code=i["statusCode"],))

        # save the list objects into the database in one query
        Message.objects.bulk_create(message_obj_list)

        return response

    except Exception as e:
        # save the sms info to the db
        sms_info_obj = SmsInfo(
            time_sent=time_sent,
            message_text=message,
            africastalking_response=e,
            success=False)
        sms_info_obj.save()
        return f"Error: {e}"
