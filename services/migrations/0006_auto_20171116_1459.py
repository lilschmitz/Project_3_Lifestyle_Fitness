# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-16 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20170404_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FilePathField(),
        ),
    ]
