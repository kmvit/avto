# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0025_auto_20170416_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='geo',
            new_name='position',
        ),
    ]