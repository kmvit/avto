# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0076_school_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='\u0421\u041c\u0421')),
            ],
            options={
                'verbose_name': '\u0428\u0430\u0431\u043b\u043e\u043d',
                'verbose_name_plural': '                 \u0421\u041c\u0421 \u0448\u0430\u0431\u043b\u043e\u043d',
            },
        ),
    ]