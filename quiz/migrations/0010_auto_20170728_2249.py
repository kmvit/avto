# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20170728_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fine',
            options={'verbose_name': '\u0428\u0442\u0440\u0430\u0444', 'verbose_name_plural': '  \u0428\u0442\u0440\u0430\u0444\u044b'},
        ),
        migrations.AlterModelOptions(
            name='fine_category',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b \u0448\u0442\u0440\u0430\u0444\u0430', 'verbose_name_plural': ' \u0420\u0430\u0437\u0434\u0435\u043b\u044b \u0448\u0442\u0440\u0430\u0444\u0430'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'verbose_name': '\u0414\u043e\u0440\u043e\u0436\u043d\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430', 'verbose_name_plural': '     \u0414\u043e\u0440\u043e\u0436\u043d\u044b\u0435 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='road_category',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0439 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438', 'verbose_name_plural': '     \u0420\u0430\u0437\u0434\u0435\u043b\u044b \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0439 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='roadsing',
            options={'verbose_name': '\u0417\u043d\u0430\u043a \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f', 'verbose_name_plural': '        \u0417\u043d\u0430\u043a\u0438 \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='roadsing_category',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b \u0437\u043d\u0430\u043a\u0430 \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f', 'verbose_name_plural': '       \u0420\u0430\u0437\u0434\u0435\u043b\u044b \u0437\u043d\u0430\u043a\u043e\u0432 \u0434\u043e\u0440\u043e\u0436\u043d\u043e\u0433\u043e \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='rule',
            options={'verbose_name': '\u041f\u0440\u0430\u0432\u0438\u043b\u043e', 'verbose_name_plural': '    \u041f\u0440\u0430\u0432\u0438\u043b\u0430'},
        ),
        migrations.AlterModelOptions(
            name='rules_category',
            options={'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b \u043f\u0440\u0430\u0432\u0438\u043b', 'verbose_name_plural': '   \u0420\u0430\u0437\u0434\u0435\u043b\u044b \u043f\u0440\u0430\u0432\u0438\u043b'},
        ),
        migrations.AddField(
            model_name='roadsing_category',
            name='slug',
            field=models.SlugField(default='sdf', verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
    ]
