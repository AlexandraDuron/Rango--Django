# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-12 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20190211_0204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
    ]