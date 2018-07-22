# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {'slug':('title',),}
    list_display = ['title','category','publish']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Faq)
