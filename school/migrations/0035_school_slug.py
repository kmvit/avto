# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-16 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0034_auto_20170416_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(default='df', unique=True, verbose_name='\u0427\u041f\u0423'),
        ),
    ]
