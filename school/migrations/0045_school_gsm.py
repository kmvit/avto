# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-27 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0044_auto_20170427_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='gsm',
            field=models.BooleanField(default=False, verbose_name='\u041e\u043d\u043b\u0430\u0439\u043d \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435'),
        ),
    ]