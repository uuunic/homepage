# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='add_temp',
            field=models.BigIntegerField(default=123),
        ),
    ]