from django.contrib import admin
from .models import User, UserInformation
from django.contrib.auth.models import Permission, Group

# Register your models here.

admin.site.register(User)
admin.site.register(Permission)


@admin.register(UserInformation)
class UserInfoAdmin(admin.ModelAdmin):
    readonly_fields = [
        "time_added",
        "time_last_edited",
    ]
