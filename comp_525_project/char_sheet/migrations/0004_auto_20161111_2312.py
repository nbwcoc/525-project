# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char_sheet', '0003_auto_20161111_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='pero',
            field=models.CharField(default='^_-', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playerclass',
            name='he',
            field=models.CharField(default='^_-', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='te',
            field=models.CharField(default='^_-', max_length=1),
            preserve_default=False,
        ),
    ]
