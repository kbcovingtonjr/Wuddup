# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carpool', '0002_auto_20170423_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='car_model_url',
            field=models.CharField(default=1, max_length=99),
            preserve_default=False,
        ),
    ]
