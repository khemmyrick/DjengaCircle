# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-10-08 00:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='classic_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
