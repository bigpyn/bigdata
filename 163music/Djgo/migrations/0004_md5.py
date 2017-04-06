# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djgo', '0003_auto_20170320_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='md5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str', models.CharField(max_length=100, unique=True)),
                ('hash_16', models.CharField(max_length=100)),
                ('hash_32', models.CharField(max_length=100)),
            ],
        ),
    ]