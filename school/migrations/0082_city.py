# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0081_auto_20180105_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430')),
                ('slug', models.SlugField(blank=True, default=None, unique=True)),
                ('description', tinymce.models.HTMLField(verbose_name='\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0431\u043b\u043e\u043a')),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '         \u0413\u043e\u0440\u043e\u0434\u0430',
            },
        ),
    ]
