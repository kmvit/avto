# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0086_school_town2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='town2',
            new_name='school_town',
        ),
        migrations.RemoveField(
            model_name='school',
            name='town',
        ),
    ]
