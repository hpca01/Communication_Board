# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expirations', '0002_drug_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='qty',
        ),
        migrations.AddField(
            model_name='expiration',
            name='facility',
            field=models.CharField(choices=[('RWC', 'Redwood City Inpatient'), ('SC', 'Santa Clara Inpatient'), ('SLN', 'San Leandro Inpatient')], default='RWC', max_length=100),
        ),
        migrations.AddField(
            model_name='expiration',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
