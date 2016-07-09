# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 06:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='create_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='member',
            name='intro_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='member',
            name='icon',
            field=models.ImageField(default='members_icon/default/icon.png', upload_to='members_icon/'),
        ),
    ]