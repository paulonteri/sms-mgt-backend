from django.contrib import admin
from .models import User, UserInformation

# Register your models here.

admin.site.register(User)


@admin.register(UserInformation)
class UserInfoAdmin(admin.ModelAdmin):
    readonly_fields = [
        "time_added",
        "time_last_edited",
    ]
