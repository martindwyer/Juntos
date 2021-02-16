from django.contrib import admin

from . import models


class GroupmemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
