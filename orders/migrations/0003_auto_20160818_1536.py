# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
