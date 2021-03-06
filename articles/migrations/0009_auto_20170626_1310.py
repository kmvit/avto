# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_auto_20170622_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='keywords',
        ),
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
