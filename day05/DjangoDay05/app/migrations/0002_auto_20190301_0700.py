# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-01 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=4),
        ),
    ]
