# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *
from school.models import Sms
from django import forms
from django.db import models
from dal import autocomplete
from django.core.mail import send_mail
import re
from urllib2 import urlopen
from urllib import quote
# Register your models here.


def make_published(modeladmin, request, queryset):
    sms = Sms.objects.get(id=1)
    phones = []
    emails = []
    for item in queryset:
        reg = re.compile('[^0-9 ]')
        phone = (reg.sub('', item.phone_number))
        phones.append(phone)
        emails.append(item.email)
    
    to = ','.join(phones)
    a = str(sms)
    subject = quote(a)

    idsender = "219D4C0A-A165-4A85-3429-6B8EC9621E25"
    #return HttpResponse(phone_number)
    url = "http://sms.ru/sms/send?api_id=%s&text=%s&to=%s" % (idsender, subject, to)
    res = urlopen(url)

    send_mail('vodibezopasno.com', u'%s' % sms, 'info@vodibezopasno.com', emails)
    
make_published.short_description = "Отправить смс"

class InstructorAdmin(admin.ModelAdmin):
    model = Instructor
    list_display = ['fio','user','city','premium']
    list_filter = ('city',)
    prepopulated_fields = {'slug': ('fio',)}
    search_fields = ['fio']
    actions = [make_published]
   
            
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(ReviewInstructor)
admin.site.register(ReviewResponceInstructor)
admin.site.register(Feedbackinstructor)