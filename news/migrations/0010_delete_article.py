# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170413_2315'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
