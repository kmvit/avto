# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from school.models import Category_education
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.shortcuts import reverse
from city.models import Town
# Create your models here.

class Instructor(models.Model):
    premium = models.BooleanField(default='False', verbose_name='Премиум аккаунт')
    date_off_premium = models.DateField(verbose_name='Дата отключения премиум',default=datetime.today, blank=True)
    user = models.ForeignKey(User,default='1', verbose_name='Владелец')
    email = models.EmailField(default='test@yandex.ru')
    instructor_town = models.ForeignKey(Town, default=2, verbose_name='Город инструктора')
    city = models.CharField(max_length=300, verbose_name ='Город')
    metro = models.CharField(max_length=300, blank=True, verbose_name ='Метро')
    fio = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    slug = models.SlugField(unique= True, verbose_name='URL')
    age = models.SmallIntegerField(verbose_name='Возраст')
    film = models.CharField(max_length=300, verbose_name='Любимый фильм')
    zodiac = models.CharField(max_length=200, verbose_name='Знак зодиака')
    smoke = models.BooleanField(default=False, verbose_name='Курение')
    experience = models.SmallIntegerField(verbose_name='Стаж вождения')
    coast = models.SmallIntegerField(verbose_name='Цена часа вождения')
    car_akpp = models.CharField(max_length=200, blank=True, verbose_name='Первый автомобиль')
    car_mkpp = models.CharField(max_length=200, blank=True, verbose_name='Второй автомобиль')
    car_learner = models.BooleanField(default=False, verbose_name='Занятия на автомобиле ученика')
    category_education = models.ManyToManyField(Category_education, verbose_name='Категория обучения', blank=True)
    credo = models.CharField(max_length=300, verbose_name='Жизненное кредо')
    hobby = models.CharField(max_length=300, verbose_name='Хобби')
    about_you = models.TextField(verbose_name='Расскажите о себе')
    about_teach = models.TextField(verbose_name='Расскажите о системе обучения')
    logo = models.ImageField(upload_to='logo', verbose_name='Ваше фото', blank = True)
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', blank=True)
    class Meta:
        verbose_name_plural = 'Инструкторы'
        verbose_name = 'Инструктор'
    def __unicode__(self):
        return self.fio
    def get_absolute_url(self):
        return reverse('profiles:profile_detail', kwargs={'pk':self.user.id})
    
class ReviewInstructor(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя')
    born = models.DateField(default=timezone.now, verbose_name='Дата создания')
    instructor = models.ForeignKey(Instructor, verbose_name='Инструктор')
    RATING_INSTRUCTOR = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_INSTRUCTOR, verbose_name='Рейтинг')
    body = models.TextField(verbose_name='Описание')
    email = models.EmailField()
    verificated = models.BooleanField(default=False, verbose_name='Активен')
    class Meta:
        verbose_name = 'Отзывы Инструкторов'
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('instructor:instructordetail', kwargs={'slug':self.instructor.slug})
    
    
class ReviewResponceInstructor(models.Model):
    review = models.ForeignKey(ReviewInstructor, verbose_name='Отзыв')
    body = models.TextField(verbose_name='Описание')
    class Meta:
        verbose_name_plural = '         Ответы на отзывы'
        verbose_name = 'Ответ на отзыв'
    def __unicode__(self):
        return u'%s' % (self.review.name)
        
class Feedbackinstructor(models.Model):
    """
    Онлайн заявки из инструкторов
    """
    name = models.CharField(max_length=300, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    instructor = models.ForeignKey(Instructor, verbose_name='Инструктор')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='                Заявки инструкторов'
        verbose_name='Заявка'
        ordering = ['-created_at']
    def __unicode__(self):
       return self.name 