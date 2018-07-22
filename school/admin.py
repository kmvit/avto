# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *
from django.db import models
from easy_maps.widgets import AddressWithMapWidget
from django import forms
from dal import autocomplete
from forms import *
from tinymce.widgets import TinyMCE
from django.core.mail import send_mail
import re
from urllib2 import urlopen
from urllib import quote
from django.contrib.admin.models import LogEntry


class AdminLogEntry(admin.ModelAdmin):
    model = LogEntry
    list_display = ['content_type','user','action_time']
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )


class BranchInline(admin.StackedInline):

    model = Branch
    extra = 0
  

class AutodromeInline(admin.StackedInline):

    model = Autodrome
    extra = 0

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0


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

    send_mail('Заявка на обучение.', u'%s' % sms, 'info@vodibezopasno.com', emails)
    
make_published.short_description = "Отправить смс"

    
class SchoolAdmin(admin.ModelAdmin):

    form = SchoolAdminForm
    model = School
    list_display = ['title','user','school_town','premium']
    list_filter = ('school_town',)
    search_fields = ['title']
    actions = [make_published]
    inlines = [BranchInline, AutodromeInline, ReviewInline]
    prepopulated_fields = {'slug': ('title',)}
    


             
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['name','school','verificated']
    list_filter = ('school','verificated')
    
    



admin.site.register(LogEntry, AdminLogEntry)
admin.site.register(School, SchoolAdmin)
admin.site.register(Branch)
admin.site.register(Document)
admin.site.register(Autodrome)
admin.site.register(Category_education)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewResponce)
admin.site.register(SchoolImage)
admin.site.register(Feedbackschool)
admin.site.register(Sms)

