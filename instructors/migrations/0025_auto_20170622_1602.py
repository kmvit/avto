# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0024_auto_20170605_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewinstructor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]