# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
from tinymce.models import HTMLField
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

class NewsCategory(models.Model):
    title = models.CharField(max_length=400, verbose_name='Название')
    slug = models.SlugField(unique=True, default="acura", verbose_name='url')
    img = models.ImageField(upload_to='avto', verbose_name='Изображение')
    class Meta:
        verbose_name_plural = 'Категории новостей'
        verbose_name = 'Категорию новости'
        ordering = ['title']
        
    def __unicode__(self):
        return u'%s' % (self.title)

class News(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    category = models.ForeignKey(NewsCategory, default=1, verbose_name='Категория')
    user = models.ForeignKey(User, verbose_name='Пользователь')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Адрес поля')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    pict = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')
    pict1 = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')
    pict2 = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')
    pict3 = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')
    pict4 = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')
    body = HTMLField(verbose_name='Содержание')
    publish = models.BooleanField(default=False, verbose_name='Опубликован')
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-born']
        
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def get_absolute_url(self):
        return reverse('news:newsdetail', kwargs={'slug':self.slug})
        
