# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170102_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(null=True, upload_to='/static/img'),
        ),
    ]
