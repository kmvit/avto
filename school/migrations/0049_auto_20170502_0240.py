# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-01 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0048_auto_20170502_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='school',
            name='med',
            field=models.BooleanField(default=False, verbose_name='\u041c\u0435\u0434.\u043a\u043e\u043c\u0438\u0441\u0441\u0438\u044f \u0432 \u0430\u0432\u0442\u043e\u0448\u043a\u043e\u043b\u0435'),
        ),
    ]