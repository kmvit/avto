# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_roadsing_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsing_category',
            name='img',
            field=models.ImageField(upload_to='roadsing', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]