# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_auto_20180129_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]