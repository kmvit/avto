# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0052_auto_20170525_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='description',
        ),
        migrations.RemoveField(
            model_name='school',
            name='keywords',
        ),
    ]
