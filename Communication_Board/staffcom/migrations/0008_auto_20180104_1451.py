# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 22:51
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('staffcom', '0007_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comm_item',
            name='descr',
            field=tinymce.models.HTMLField(),
        ),
    ]
