# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-02 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0075_auto_20171101_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='test@yandex.ru', max_length=254),
        ),
    ]
