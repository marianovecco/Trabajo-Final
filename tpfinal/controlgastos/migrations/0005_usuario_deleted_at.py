# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlgastos', '0004_auto_20171130_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
