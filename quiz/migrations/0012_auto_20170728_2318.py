# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_roadsing_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsing',
            name='number',
            field=models.CharField(max_length=12, verbose_name='\u041d\u043e\u043c\u0435\u0440'),
        ),
    ]