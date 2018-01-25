# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-03 06:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staffcom', '0006_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
