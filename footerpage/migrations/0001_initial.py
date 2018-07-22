# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-15 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(unique=True)),
                ('body', tinymce.models.HTMLField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '                \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u043e\u0434\u0432\u0430\u043b\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u043f\u043e\u0434\u0432\u0430\u043b\u0430',
            },
        ),
    ]
