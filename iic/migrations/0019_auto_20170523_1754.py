# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-23 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iic', '0018_remove_pageinput_trigger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageinput',
            old_name='bridge_trigger',
            new_name='trigger',
        ),
    ]
