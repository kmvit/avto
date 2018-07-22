# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 21:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440')),
                ('premium', models.BooleanField(default=False, verbose_name='\u041f\u0440\u0435\u043c\u0438\u0443\u043c \u0430\u043a\u043a\u0430\u0443\u043d\u0442')),
                ('date_premium_on', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0435\u043c\u0438\u0443\u043c')),
                ('date_premium_off', models.DateField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0435\u043c\u0438\u0443\u043c')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
        ),
    ]