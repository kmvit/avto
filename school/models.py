# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from tinymce.models import HTMLField
import geocoder
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.shortcuts import reverse
from django.urls import reverse_lazy
from city.models import *
# Create your models here.

def get_upload_path(instance, filename):
    return (u'%s' % filename).encode('utf-8')

class Document(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    file = models.FileField(upload_to=get_upload_path, verbose_name='Документы')
    class Meta:
        verbose_name_plural = '       Документы для скачивания'
        verbose_name = 'Документ'
    def __unicode__(self):
        return u'%s' % (self.title)
        

        

class Category_education(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название')
    class Meta:
        verbose_name_plural = '      Категории обучения'
        verbose_name = 'Категория обучения'
    def __unicode__(self):
        return u'%s' % (self.title)
    
    
class School(models.Model):
    user = models.ForeignKey(User, default='1', verbose_name='Владелец')
    email = models.EmailField(default='test@yandex.ru')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ')
    premium = models.BooleanField(default=False, verbose_name='Премиум')
    text_unique_price = models.CharField(max_length=1000, verbose_name='Текст для поля уникальной цены', blank=True)
    date_off_premium = models.DateField(verbose_name='Дата отключения премиум',default=datetime.today, blank=True)
    title = models.CharField(max_length=300, verbose_name='Название')
    site = models.URLField(max_length=200, verbose_name='Адрес сайта', blank=True)
    cost = models.PositiveIntegerField(verbose_name='Цена обучения', blank=True)
    gsm = models.BooleanField(default=False, verbose_name='Включая ГСМ')
    term = models.CharField(max_length=4, verbose_name='Срок обучения', blank=True)
    category_education = models.ManyToManyField(Category_education, verbose_name='Категория обучения', blank=True)
    photograph = models.BooleanField(default=False, verbose_name='Фотограф')
    med = models.BooleanField(default=False, verbose_name='Мед.комиссия в автошколе')
    online = models.BooleanField(default=False, verbose_name='Онлайн обучение')
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    city = models.CharField(max_length=300, verbose_name="Город", default='Москва')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', blank=True)
    logo = models.ImageField(upload_to='logo', blank=True, verbose_name='Лого')
    body = HTMLField(verbose_name='Содержание')
    school_town = models.ForeignKey(Town, default=122, verbose_name='Город')
    metro = models.CharField(max_length=300, blank=True, verbose_name ='Метро')
    vk = models.CharField(max_length=300, blank=True, verbose_name='Группа в Вконтакте')
    od = models.CharField(max_length=300, blank=True, verbose_name='Группа в Одноклассниках')
    fc = models.CharField(max_length=300, blank=True, verbose_name='Группа в Фэйсбук')
    tw = models.CharField(max_length=300, blank=True, verbose_name='Группа в Твитере')
    class Meta:
        verbose_name_plural = ' Школы'
        verbose_name = 'Школа'
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def mygeo(self):
        g = geocoder.google(self.adress)
        return g.latlng
        
    def save(self):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(School, self).save()
        
    def get_absolute_url(self):
        return reverse('school:schooldetail', kwargs={'slug':self.slug})
        
class Branch(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    school = models.ForeignKey(School, verbose_name='Школа')
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', blank=True)
    metro = models.CharField(max_length=300, blank = True, verbose_name = 'Метро')
    description_adress = models.CharField(max_length=500, verbose_name='Описание')
    class Meta:
        verbose_name_plural = '  Филиалы'
        verbose_name = 'Филиал'
    def __unicode__(self):
        return u'%s' % (self.title)
    def get_absolute_url(self):
        return reverse('profiles:profile_branch_list', kwargs={'pk':self.school.user.id, 'slug':self.school.slug})

class Autodrome(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    school = models.ForeignKey(School, verbose_name='Школа')
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    metro = models.CharField(max_length=300, blank = True, verbose_name = 'Метро')
    description_adress = models.CharField(max_length=500, verbose_name='Описание')
    class Meta:
        verbose_name_plural = '   Автодромы'
        verbose_name = 'Автодром'
    def __unicode__(self):
        return u'%s' % (self.title)
    def get_absolute_url(self):
        return reverse('profiles:profile_branch_list', kwargs={'pk':self.school.user.id, 'slug':self.school.slug})
        
class Review(models.Model):
    """
    Отзыв с оценкой
    """
    name = models.CharField(max_length=300, verbose_name='Имя')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    school = models.ForeignKey(School, verbose_name='Школа')
    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default='5', verbose_name='Рейтинг')
    body = models.TextField(verbose_name='Описание')
    email = models.EmailField()
    verificated = models.BooleanField(default=False, verbose_name='Активен')
    class Meta:
        verbose_name_plural = '    Отзывы'
        verbose_name = 'Отзыв'
    def __unicode__(self):
        return u'%s' % (self.name)

    def school_list(self):
        rew_all_sum = Review.objects.aggregate(Sum('rating')).values()[0]
        rew_all_count = Review.objects.filter(school__slug=self.kwargs['slug']).count()
    def get_absolute_url(self):
        return reverse('school:schooldetail', kwargs={'slug':self.school.slug})
        
class ReviewResponce(models.Model):
    """
    Ответ на отзыв с оценкой
    """
    review = models.ForeignKey(Review, verbose_name='Отзыв')
    body = models.TextField(verbose_name='Описание')
    class Meta:
        verbose_name_plural = '         Ответы на отзывы'
        verbose_name = 'Ответ на отзыв'
    def __unicode__(self):
        return u'%s' % (self.review.name)
    

class SchoolImage(models.Model):
    school = models.ForeignKey(School)
    pict = models.ImageField(max_length=300, verbose_name='Изображение')
    class Meta:
        verbose_name = '     Фото школы'
    def __unicode__(self):
        return u'%s' % (self.id)    
    def get_absolute_url(self):
        return reverse('profiles:profile_schoolimage_list', kwargs={'pk':self.school.user.id, 'slug':self.school.slug})
        
class SchoolDocument(models.Model):
    """
    Возможность загрузить изображения лицензий
    """
    title = models.CharField(max_length=300, verbose_name='Название')
    img = models.ImageField(upload_to=get_upload_path, verbose_name='Документы')
    school = models.ForeignKey(School, verbose_name='Школа')
    class Meta:
        verbose_name_plural = '        Документы автошкол'
        verbose_name = 'Документ'
        
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def get_absolute_url(self):
        return reverse('profiles:profile_schooldocument_list', kwargs={'pk':self.school.user.id, 'slug':self.school.slug})
        
class Feedbackschool(models.Model):
    """
    Онлайн заявки из школ
    """
    name = models.CharField(max_length=300, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    school = models.ForeignKey(School, verbose_name='Школа')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='                Заявки автошкол'
        verbose_name='Заявка'
        ordering = ['-created_at']
    def __unicode__(self):
       return self.name 
       
       
class Sms(models.Model):
    title = models.CharField(max_length=300, verbose_name='СМС')
    class Meta:
        verbose_name_plural='                 СМС шаблон'
        verbose_name='Шаблон'
    def __unicode__(self):
       return u'%s' % (self.title)