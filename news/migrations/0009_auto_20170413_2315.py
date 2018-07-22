# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170413_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='url', unique=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044f'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044f'),
        ),
    ]