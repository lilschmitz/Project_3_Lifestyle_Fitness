# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170401_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
    ]
