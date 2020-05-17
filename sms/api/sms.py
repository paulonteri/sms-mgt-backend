from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from sms.services.sms import send_sms, send_to_all_contacts, send_to_tags


class SendSms(APIView):
    """
    Send SMS API
    """

    def post(self, request, format=None):
        sms = request.data
        return Response(
            send_sms(recipients=sms["recipients"], message=sms["message"])
        )


class SmsAllContactsAPI(APIView):
    """
    Send SMS to all contacts
    """

    def post(self, request, format=None):
        try:
            send_to_all_contacts(request.data["message"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")


class SmsTagsAPI(APIView):
    """
    Send SMS to all contacts within specific tags
    """

    def post(self, request, format=None):
        try:
            send_to_tags(message=request.data["message"], tags=request.data["tags"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")
