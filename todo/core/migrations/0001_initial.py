# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=75, unique=True)),
                ('beschrijving', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]