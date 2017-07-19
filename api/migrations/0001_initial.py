# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-23 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NodeSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('URL', models.CharField(max_length=250)),
                ('use_ssl', models.BooleanField(default=False)),
                ('cert_path', models.CharField(blank=True, max_length=200, null=True)),
                ('key_path', models.CharField(blank=True, max_length=200, null=True)),
                ('ca_path', models.CharField(blank=True, max_length=200, null=True)),
                ('api_key', models.CharField(blank=True, max_length=200, null=True)),
                ('timeout_time', models.IntegerField(blank=True, help_text=b'In Seconds', null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('node_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NodeStatus')),
            ],
        ),
    ]
