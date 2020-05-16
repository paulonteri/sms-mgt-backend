from django.urls import path
from sms.api.sms import SendSms, SmsAllContactsAPI


urlpatterns = [
    path('send/', SendSms.as_view()),
    path('contacts/all/', SmsAllContactsAPI.as_view()),
]
