# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0051_auto_20170525_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo', verbose_name='\u041b\u043e\u0433\u043e'),
        ),
    ]