# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-12 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180911_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='pics/%D/'),
        ),
    ]
