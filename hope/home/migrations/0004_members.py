# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160707_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.ImageField(default='members_icon/xxx/icon.png', upload_to='members_icon/')),
            ],
        ),
    ]
