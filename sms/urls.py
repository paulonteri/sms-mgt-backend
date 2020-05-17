from django.urls import path
from sms.api.sms import SendSms, SmsAllContactsAPI, SmsTagsAPI, SmsContactAPI

urlpatterns = [
    path('send/', SendSms.as_view()),
    path('contacts/all/', SmsAllContactsAPI.as_view()),
    path('contacts/tags/', SmsTagsAPI.as_view()),
    path('contacts/contact/', SmsContactAPI.as_view()),
]
