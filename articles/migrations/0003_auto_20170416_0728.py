# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20170416_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.CharField(max_length=300),
        ),
    ]
