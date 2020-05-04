from django.db import models


class SmsInfo(models.Model):
    """
    general information about a group of SMS(s) is sent
    created per Africa'sTalking send SMS API call
    """
    success = models.BooleanField(
        default=False, editable=False, null=True)  # check whether message(s) sent successfully
    message_text = models.CharField(
        max_length=255, editable=False, null=True)  # actual sms messge text sent
    africastalking_response = models.CharField(
        max_length=255,  editable=False, null=True)  # response massage received from africastalking
    # time message(s) finished sending
    time_sent = models.DateTimeField(editable=False, null=True)
    time_added = models.DateTimeField(
        auto_now_add=True)  # when the message object is first created
    time_last_edited = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ["time_last_edited"]


class Message(models.Model):
    """
    information about a single SMS sent to a single receiver
    """
    message_info = models.ForeignKey(
        SmsInfo, on_delete=models.CASCADE, editable=False)
    message_id = models.CharField(max_length=255, editable=False)
    status_code = models.CharField(max_length=255, editable=False)
    number = models.CharField(max_length=255, editable=False)
    cost = models.CharField(max_length=255, editable=False)
    status = models.CharField(max_length=255, editable=False)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'message_info'
