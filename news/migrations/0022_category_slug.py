# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20171008_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='acura', unique=True, verbose_name='url'),
        ),
    ]
