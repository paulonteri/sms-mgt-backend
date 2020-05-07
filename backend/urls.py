from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/sms/', include('sms.urls')),
    path('api/v1/contacts/', include('contacts.urls')),

]
