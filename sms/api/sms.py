

from rest_framework import permissions
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView


from sms.services.africastalking_api import send_sms
from sms.services.sms import send_to_all_contacts, send_to_tags, send_to_contact


# from rest_framework import permissions


class SendSms(APIView):
    """
    Send SMS API
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if not (request.user.has_perms('sms.add_message', 'sms.view_message') or
                request.user.has_perms('sms.add_smsinfo', 'sms.view_smsinfo') or
                request.user.has_perms('contacts.view_contact')):
            raise PermissionDenied()
        sms = request.data
        return Response(
            send_sms(user=self.request.user, recipients=sms["recipients"], message=sms["message"])
        )


class SmsAllContactsAPI(APIView):
    """
    Send SMS to all contacts
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if not (request.user.has_perms('sms.add_message', 'sms.view_message') or
                request.user.has_perms('sms.add_smsinfo', 'sms.view_smsinfo') or
                request.user.has_perms('contacts.view_contact')):
            raise PermissionDenied()
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
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if not (request.user.has_perms('sms.add_message', 'sms.view_message') or
                request.user.has_perms('sms.add_smsinfo', 'sms.view_smsinfo') or
                request.user.has_perms('contacts.view_contact')):
            raise PermissionDenied()
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
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if not (request.user.has_perms('sms.add_message', 'sms.view_message') or
                request.user.has_perms('sms.add_smsinfo', 'sms.view_smsinfo') or
                request.user.has_perms('contacts.view_contact')):
            raise PermissionDenied()

        try:
            send_to_contact(user=self.request.user, message=request.data["message"], contact=request.data["contact"])
        except Exception as error:
            raise APIException(error)
        else:
            return Response("SMSs sent")
