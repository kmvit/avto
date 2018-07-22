# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
 
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bill)
admin.site.register(Social)