# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    model = News
    prepopulated_fields = {'slug':('title',),}
    list_display = ['title','publish']

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory)
