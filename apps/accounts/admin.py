from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    """ class registers the profile picture field with User """
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Additional Profile Info',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'profile_pic',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)