# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170108_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='year',
        ),
        migrations.AddField(
            model_name='statistic',
            name='year',
            field=models.ManyToManyField(blank=True, null=True, to='core.Year'),
        ),
    ]
