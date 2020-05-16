from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class SmsInfoAdmin(admin.ModelAdmin):

    readonly_fields = [
        "time_added",
        "time_last_edited",
    ]
