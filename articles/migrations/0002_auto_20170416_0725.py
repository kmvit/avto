# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', max_length=300),
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(default='\u041a\u043b\u044e\u0447\u0438', max_length=300),
        ),
    ]
