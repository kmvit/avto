# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-11 15:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0078_remove_feedbackschool_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackschool',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
