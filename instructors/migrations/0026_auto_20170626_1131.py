# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0025_auto_20170622_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo', verbose_name='\u0412\u0430\u0448\u0435 \u0444\u043e\u0442\u043e'),
        ),
    ]
