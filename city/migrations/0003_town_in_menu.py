# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20180126_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='in_menu',
            field=models.BooleanField(default=False),
        ),
    ]
