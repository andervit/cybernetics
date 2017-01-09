# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='media')),
            ],
        ),
    ]
