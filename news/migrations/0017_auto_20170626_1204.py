# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20170626_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-born'], 'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d'),
        ),
    ]
