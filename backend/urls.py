from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def pong(request):
    return HttpResponse("pong")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ping/', pong),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/sms/', include('sms.urls')),
    path('api/v1/contacts/', include('contacts.urls')),
    path('api/v1/finance/', include('finance.urls')),

]
