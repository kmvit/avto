# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 20:51
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0082_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a'),
        ),
    ]
