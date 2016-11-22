# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('char_sheet', '0010_auto_20161120_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='versatile_damage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='armor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='char_sheet.Armor'),
        ),
        migrations.AlterField(
            model_name='item',
            name='attack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='char_sheet.Attack'),
        ),
        migrations.AlterField(
            model_name='race',
            name='subrace_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='char_sheet.Race'),
        ),
    ]
