# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char_sheet', '0005_auto_20161111_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alignment',
            field=models.CharField(max_length=2),
        ),
    ]
