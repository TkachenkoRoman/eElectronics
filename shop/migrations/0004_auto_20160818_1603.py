# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160818_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.FloatField(),
        ),
    ]
