# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-16 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0030_remove_city_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='position',
        ),
        migrations.RemoveField(
            model_name='school',
            name='position',
        ),
    ]
