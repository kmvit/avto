# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20170413_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='adress',
            field=models.CharField(default='\u041c\u043e\u0441\u043a\u0432\u0430, \u041b\u0435\u043d\u0438\u043d\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 31', max_length=300, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
    ]