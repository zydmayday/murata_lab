# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160709_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='icon',
            field=models.ImageField(default='member/static/images/members_icon/default/icon.png', upload_to='member/static/images/members_icon/'),
        ),
    ]