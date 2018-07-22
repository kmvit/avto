# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u043e\u0442\u0432\u0435\u0442\u0430', max_length=1000, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
                ('correct', models.BooleanField(default=False, help_text='\u042d\u0442\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442?', verbose_name='\u0412\u0435\u0440\u043d\u043e')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('answer_order', models.CharField(blank=True, choices=[('content', '\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'), ('random', '\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u043e'), ('none', '\u041d\u0435\u0442')], help_text='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432', max_length=30, null=True, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441 \u0441 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u043c\u0438 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430\u043c\u0438 \u043e\u0442\u0432\u0435\u0442\u043e\u0432',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0441 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u043c\u0438 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430\u043c\u0438 \u043e\u0442\u0432\u0435\u0442\u043e\u0432',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multichoice.MCQuestion', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
        ),
    ]