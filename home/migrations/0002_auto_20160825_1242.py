# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
    ]
