from django.urls import path

from finance.api import GetBalanceAPI

urlpatterns = [
    path('balance', GetBalanceAPI.as_view(), name='Get Balance'),
]
