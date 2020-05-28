from datetime import datetime

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Contact
from sms.models import Message, SmsInfo
from sms.services.africastalking_api import send_sms
from sms.services.sms import send_to_all_contacts, send_to_tags, send_to_contact


# from rest_framework import permissions


class SendSms(APIView):
    """
    Send SMS API
    """

    def get_queryset(self):
        c = Contact.objects.filter(time_added__gt=datetime.now())
        m = Message.objects.filter(time_added__gt=datetime.now())
        s = SmsInfo.objects.filter(time_added__gt=datetime.now())
        return c.union(m, s)

    def post(self, request, format=None):
        sms = request.data
        return Response(
            send_sms(user=self.request.user, recipients=sms["recipients"], message=sms["message"])
        )


class SmsAllContactsAPI(APIView):
    """
    Send SMS to all contacts
    """

    def get_queryset(self):
        c = Contact.objects.filter(time_added__gt=datetime.now())
        m = Message.objects.filter(time_added__gt=datetime.now())
        s = SmsInfo.objects.filter(time_added__gt=datetime.now())
        return c.union(m, s)

    def post(self, request, format=None):
        try:
            send_to_all_contacts(user=self.request.user, message=request.data["message"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")


class SmsTagsAPI(APIView):
    """
    Send SMS to all contacts within specific tags
    """

    def get_queryset(self):
        c = Contact.objects.filter(time_added__gt=datetime.now())
        m = Message.objects.filter(time_added__gt=datetime.now())
        s = SmsInfo.objects.filter(time_added__gt=datetime.now())
        return c.union(m, s)

    def post(self, request, format=None):
        try:
            send_to_tags(user=self.request.user, message=request.data["message"], tags=request.data["tags"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")


class SmsContactAPI(APIView):
    """
    Send SMS to all contacts
    """

    def get_queryset(self):
        c = Contact.objects.filter(time_added__gt=datetime.now())
        m = Message.objects.filter(time_added__gt=datetime.now())
        s = SmsInfo.objects.filter(time_added__gt=datetime.now())
        return c.union(m, s)

    def post(self, request, format=None):
        try:
            send_to_contact(user=self.request.user, message=request.data["message"], contact=request.data["contact"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")
