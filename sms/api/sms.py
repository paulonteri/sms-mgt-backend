from rest_framework.views import APIView
from rest_framework.response import Response
from sms.services.sms import send_sms


class SendSms(APIView):
    """
    Send SMS API
    """

    def post(self, request, format=None):
        sms = request.data
        return Response(
            send_sms(recipients=sms["recipients"], message=sms["message"])
        )
