# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 22:15
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0043_auto_20170420_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'),
        ),
    ]