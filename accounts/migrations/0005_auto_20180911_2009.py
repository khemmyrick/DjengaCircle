# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-12 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180911_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]
