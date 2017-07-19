# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-08 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_paymentoption_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to=b'crm_productitem_imagepath/')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='image_path',
            new_name='default_image',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='institution_till',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductItem'),
        ),
    ]
