# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-04 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_regul'),
    ]

    operations = [
        migrations.AddField(
            model_name='regul',
            name='slug',
            field=models.SlugField(default='regul', verbose_name='url'),
        ),
    ]