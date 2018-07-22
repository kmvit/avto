# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.db import models

# Create your models here.

class Town(models.Model):
    title = models.CharField(max_length=310, verbose_name='Название города')
    slug = models.SlugField(unique = True, default=None, blank=True)
    description = HTMLField(verbose_name='Текстовый блок', blank=True)
    description_instructor = HTMLField(verbose_name='Текстовый блок инструктора', blank=True)
    in_menu = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '         Города'
        verbose_name = 'Город'
        ordering = ['title']
    def __unicode__(self):
        return u'%s' % (self.title)
        
    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Town, self).save()
    