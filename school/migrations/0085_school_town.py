# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0084_auto_20180125_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='town',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.City'),
        ),
    ]
