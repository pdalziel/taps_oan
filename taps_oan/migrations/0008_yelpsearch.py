# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taps_oan', '0007_auto_20170223_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='YelpSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
