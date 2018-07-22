# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    CHOICES = (
        ('1','Инструктор'),
        ('2', 'Автошкола'),
        ('3', 'Отзывы'),
        )
    status = models.CharField(blank=True, max_length=1, choices=CHOICES, default=3,verbose_name='Статус пользователя') 
    premium = models.BooleanField(default=False, verbose_name='Премиум аккаунт')
    date_premium_on = models.DateField(blank=True, default=timezone.now, verbose_name='Дата включения премиум')
    date_premium_off = models.DateField(blank=True, default=timezone.now, verbose_name='Дата отключения премиум')
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __unicode__(self):
        return u'%s' % self.user.email
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
class Bill(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    name = models.CharField(max_length=400, verbose_name='Наименование')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    kpp = models.CharField(max_length=100, verbose_name='КПП')
    bik = models.CharField(max_length=12, blank=True, verbose_name='БИК')
    bank = models.CharField(max_length=100, verbose_name='Банк')
    raschet_bill = models.CharField(max_length=25, verbose_name='Расчетный счет')
    zip_address = models.CharField(max_length=500, verbose_name='Почтовый адрес')
    email = models.EmailField()
    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profiles:profile_detail', kwargs={'pk': self.user.id})
        

class Social(models.Model):
    title = models. CharField(max_length=300, verbose_name='Социальные сети')
    url = models.CharField(max_length=300, verbose_name='Ссылка')
    class Meta:
        verbose_name = 'Социальную сеть'
        verbose_name_plural = 'Социальные сети'
        
    def __unicode__(self):
        return self.title