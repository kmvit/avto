# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-01 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20171008_0136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscategory',
            options={'ordering': ['title'], 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u043d\u043e\u0432\u043e\u0441\u0442\u0438', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439'},
        ),
    ]