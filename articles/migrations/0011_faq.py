# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-07 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0010_auto_20170724_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('question', tinymce.models.HTMLField(verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441')),
                ('answer', tinymce.models.HTMLField(blank=True, verbose_name='\u041e\u0442\u0432\u0435\u0442')),
                ('public', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441-\u043e\u0442\u0432\u0435\u0442',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b-\u043e\u0442\u0432\u0435\u0442\u044b',
            },
        ),
    ]
