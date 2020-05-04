from django.urls import path, include
from sms.api.sms import SendSms


urlpatterns = [
    path('send/', SendSms.as_view()),
]
