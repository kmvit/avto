# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0022_auto_20170528_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewinstructor',
            name='user',
        ),
    ]
