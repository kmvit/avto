# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_school_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='region',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
