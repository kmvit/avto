# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-18 20:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0091_auto_20180218_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='date_off_premium',
            field=models.DateField(blank=True, default=datetime.datetime.today, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0435\u043c\u0438\u0443\u043c'),
        ),
    ]
