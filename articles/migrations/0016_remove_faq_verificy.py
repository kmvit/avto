# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-11 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_faq_verificy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='verificy',
        ),
    ]
