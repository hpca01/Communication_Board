# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 00:01
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('staffcom', '0008_auto_20180104_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]