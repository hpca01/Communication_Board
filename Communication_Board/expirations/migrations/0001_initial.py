# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Expiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entered', models.DateField(auto_now=True)),
                ('expirationDate', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField()),
                ('drug_Linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expiration_dates', to='expirations.Drug')),
            ],
        ),
    ]