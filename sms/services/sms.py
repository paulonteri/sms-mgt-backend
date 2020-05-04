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
    try:
        # buy a Dedicated Short Code to get a sender ID
        # response = sms.send(message, recipients, sender)
        response = sms.send(message, recipients)
        return response
    except Exception as e:
        return f"Error: {e}"

