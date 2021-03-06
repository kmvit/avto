# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-01 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0072_reviewresponce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbackscholl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='\u0418\u043c\u044f')),
                ('phone', models.CharField(max_length=12, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Category_education', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School', verbose_name='\u0428\u043a\u043e\u043b\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '                \u0417\u0430\u044f\u0432\u043a\u0438 \u0430\u0432\u0442\u043e\u0448\u043a\u043e\u043b',
            },
        ),
    ]
