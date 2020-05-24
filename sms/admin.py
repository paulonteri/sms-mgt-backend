from django.contrib import admin
from sms.models import SmsInfo, Message


@admin.register(SmsInfo)
class SmsInfoAdmin(admin.ModelAdmin):

    readonly_fields = [
        "success",
        "user",
        "message_text",
        "africastalking_response",
        "time_sent",
        "time_added",
        "time_last_edited",
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    readonly_fields = [
        "message_info",
        "message_id",
        "status_code",
        "number",
        "cost",
        "time_added",
        "time_last_edited",
    ]
