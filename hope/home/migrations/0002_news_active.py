# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='active',
            field=models.IntegerField(default=1),
        ),
    ]
