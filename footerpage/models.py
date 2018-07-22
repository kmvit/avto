# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(unique=True)
    body = HTMLField(verbose_name='Содержание')
    class Meta:
        verbose_name = 'Страницу подвала'
        verbose_name_plural = '                 Страницы подвала'
    
    def __unicode__(self):
        return self.title