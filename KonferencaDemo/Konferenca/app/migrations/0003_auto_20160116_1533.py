# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160116_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='session',
            name='twitter',
        ),
        migrations.AddField(
            model_name='speaker',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='speaker',
            name='twitter',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
