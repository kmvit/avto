# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20170413_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='school',
            name='description_adress',
            field=models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u0434\u0440\u0435\u0441\u0430'),
        ),
    ]
