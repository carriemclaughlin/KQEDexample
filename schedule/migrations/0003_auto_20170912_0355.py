# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_collection_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='ordinal',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='season',
            name='slug',
        ),
    ]
