# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-23 14:52
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('upc', '0001_initial'),
        ('crm', '0001_initial'),
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('credit', models.BooleanField(default=False)),
                ('transaction_reference', models.CharField(blank=True, max_length=45, null=True)),
                ('action_reference', models.CharField(blank=True, max_length=45, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('balance_bf', models.DecimalField(decimal_places=2, max_digits=19)),
                ('pn', models.BooleanField(default=False, help_text=b'Push Notification', verbose_name=b'Push Notification')),
                ('pn_ack', models.BooleanField(default=False, help_text=b'Push Notification Acknowledged', verbose_name=b'Push Notification Acknowledged')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=19)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('other_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('other_relief', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('details', models.CharField(max_length=1920)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('pn', models.BooleanField(default=False, help_text=b'Push Notification', verbose_name=b'Push Notification')),
                ('pn_ack', models.BooleanField(default=False, help_text=b'Push Notification Acknowledged', verbose_name=b'Push Notification Acknowledged')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Channel')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('gateway_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.GatewayProfile')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductItem')),
            ],
        ),
        migrations.CreateModel(
            name='CartStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('reference', models.CharField(max_length=45)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('expiry', models.DateTimeField()),
                ('cart_processed', models.BooleanField(default=False)),
                ('cart_item', models.ManyToManyField(to='pos.CartItem')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('gateway_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.GatewayProfile')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.OrderStatus')),
            ],
        ),
        migrations.CreateModel(
            name='SaleCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('credit', models.BooleanField(default=False)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('charge_value', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('is_percentage', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('per_item', models.BooleanField(default=False)),
                ('gateway', models.ManyToManyField(blank=True, to='administration.Gateway')),
                ('institution', models.ManyToManyField(blank=True, to='upc.Institution')),
                ('payment_method', models.ManyToManyField(blank=True, to='bridge.PaymentMethod')),
                ('product_type', models.ManyToManyField(blank=True, to='crm.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='SaleChargeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductItem')),
            ],
        ),
        migrations.CreateModel(
            name='SaleContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('sale_contact_number', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=256, null=True)),
                ('details', models.CharField(max_length=1280)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salecontact__created_by', to='upc.GatewayProfile')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
                ('primary_contact_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='SaleContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
            ],
        ),
        migrations.AddField(
            model_name='salecontact',
            name='sale_contact_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.SaleContactType'),
        ),
        migrations.AddField(
            model_name='salecharge',
            name='sale_charge_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.SaleChargeType'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.CartStatus'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='till',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.InstitutionTill'),
        ),
        migrations.AddField(
            model_name='billmanager',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='billmanager',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge.PaymentMethod'),
        ),
    ]
