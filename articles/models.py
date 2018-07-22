# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='url')
    class Meta:
        verbose_name_plural = 'Категория статьи'
        verbose_name = 'Категорию статьи'
    def __unicode__(self):
        return u'%s' % (self.title)

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    user = models.ForeignKey(User, verbose_name='Пользователь')
    category = models.ForeignKey(Category, verbose_name='Категория')
    slug = models.SlugField(max_length=50, default='url', unique=True, verbose_name='Адрес поля')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    pict = models.ImageField(upload_to='news', verbose_name='Изображение')
    pict1 = models.ImageField(upload_to='news', blank= True, verbose_name='Изображение')
    pict2 = models.ImageField(upload_to='news', blank= True, verbose_name='Изображение')
    pict3 = models.ImageField(upload_to='news', blank= True, verbose_name='Изображение')
    pict4 = models.ImageField(upload_to='news', blank= True, verbose_name='Изображение')
    body = HTMLField(verbose_name='Содержание')
    publish = models.BooleanField(default=False, verbose_name='Опубликован')
    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-born']
    def __unicode__(self):
        return u'%s' % (self.title)
    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'category_slug':self.category.slug,'slug':self.slug})
        

class Faq(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    question = HTMLField(verbose_name='Вопрос')
    answer = HTMLField(blank=True, verbose_name='Ответ')
    public = models.BooleanField(default=False, verbose_name="Опубликовать")
    class Meta:
        verbose_name_plural = 'Вопросы-ответы'
        verbose_name = 'Вопрос-ответ'
        ordering = ['-born']
    def __unicode__(self):
        return u'%s' % (self.name)