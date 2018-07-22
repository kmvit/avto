# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-01 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0061_auto_20170801_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk', models.CharField(blank=True, max_length=300, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0432 \u0412\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435')),
                ('od', models.CharField(blank=True, max_length=300, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0432 \u041e\u0434\u043d\u043e\u043a\u043b\u0430\u0441\u0441\u043d\u0438\u043a\u0430\u0445')),
                ('fc', models.CharField(blank=True, max_length=300, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0432 \u0424\u044d\u0439\u0441\u0431\u0443\u043a')),
                ('tw', models.CharField(blank=True, max_length=300, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0432 \u0422\u0432\u0438\u0442\u0435\u0440\u0435')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0443 \u0441 \u0441\u043e\u0446 \u0441\u0435\u0442\u044f\u0445',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0432 \u0441\u043e\u0446 \u0441\u0435\u0442\u044f\u0445',
            },
        ),
        migrations.RemoveField(
            model_name='school',
            name='fc',
        ),
        migrations.RemoveField(
            model_name='school',
            name='od',
        ),
        migrations.RemoveField(
            model_name='school',
            name='tw',
        ),
        migrations.RemoveField(
            model_name='school',
            name='vk',
        ),
        migrations.AddField(
            model_name='social_group',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', verbose_name='\u0428\u043a\u043e\u043b\u0430'),
        ),
    ]