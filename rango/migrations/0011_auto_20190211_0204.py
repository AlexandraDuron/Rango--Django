# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-11 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_auto_20190211_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
