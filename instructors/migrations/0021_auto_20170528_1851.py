# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0020_auto_20170502_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='keywords',
        ),
    ]