# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_category_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='NewsCategory',
        ),
    ]
