# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-23 14:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('upc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('record', models.CharField(blank=True, max_length=200, null=True)),
                ('alias', models.CharField(max_length=50)),
                ('enrollment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_source_capacity_min', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('product_source_capacity_max', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('default_image', models.ImageField(blank=True, max_length=200, null=True, upload_to=b'productitem_default_image/')),
                ('product_path', models.FileField(blank=True, max_length=200, null=True, upload_to=b'productitem_product_path/')),
                ('product_url', models.CharField(blank=True, max_length=400, null=True)),
                ('condition', models.CharField(blank=True, max_length=200, null=True)),
                ('feature', models.CharField(blank=True, max_length=200, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200, null=True)),
                ('manufactured', models.DateField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=1240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('si_unit', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_alias', models.CharField(blank=True, max_length=200, null=True)),
                ('account_record', models.CharField(max_length=50)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='NominationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_alias', models.CharField(blank=True, max_length=200, null=True)),
                ('account_record', models.CharField(max_length=50)),
                ('gateway_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.GatewayProfile')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOptionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=45, null=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Industry')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCharge',
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
                ('for_float', models.NullBooleanField(default=False)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('institution', models.ManyToManyField(blank=True, to='upc.Institution')),
                ('payment_method', models.ManyToManyField(blank=True, to='bridge.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('coupon', models.CharField(blank=True, max_length=45, null=True)),
                ('credit', models.BooleanField(default=False)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('charge_value', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('is_percentage', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('for_float', models.NullBooleanField(default=False)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('institution', models.ManyToManyField(blank=True, to='upc.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_limit_min', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('unit_limit_max', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('variable_unit', models.NullBooleanField(default=False)),
                ('float_limit_min', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('float_limit_max', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('float_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('institution_url', models.CharField(blank=True, max_length=640, null=True)),
                ('institution_username', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('institution_password', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('image_path', models.FileField(blank=True, max_length=200, null=True, upload_to=b'crm_productitem_imagepath/')),
                ('uneditable', models.BooleanField(default=False)),
                ('kind', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
                ('institution_till', models.ManyToManyField(blank=True, to='upc.InstitutionTill')),
                ('product_display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductDisplay')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('institution_till', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.InstitutionTill')),
                ('metric', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Metric')),
                ('payment_method', models.ManyToManyField(blank=True, to='bridge.PaymentMethod')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductCategory')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge.Service')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductStatus')),
            ],
        ),
        migrations.CreateModel(
            name='RecurrentService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('request', models.CharField(max_length=1920)),
                ('request_auth', models.BooleanField(default=False)),
                ('scheduled_send', models.DateTimeField()),
                ('scheduled_days', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Currency')),
                ('enrollment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Enrollment')),
                ('nomination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Nomination')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge.Service')),
            ],
        ),
        migrations.CreateModel(
            name='RecurrentServiceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='recurrentservice',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.RecurrentServiceStatus'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductStatus'),
        ),
        migrations.AddField(
            model_name='productionfrequency',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductStatus'),
        ),
        migrations.AddField(
            model_name='productdiscount',
            name='product_type',
            field=models.ManyToManyField(blank=True, to='crm.ProductType'),
        ),
        migrations.AddField(
            model_name='productdiscount',
            name='till',
            field=models.ManyToManyField(blank=True, to='upc.InstitutionTill'),
        ),
        migrations.AddField(
            model_name='productcharge',
            name='product_type',
            field=models.ManyToManyField(blank=True, to='crm.ProductType'),
        ),
        migrations.AddField(
            model_name='productcharge',
            name='till',
            field=models.ManyToManyField(blank=True, to='upc.InstitutionTill'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductStatus'),
        ),
        migrations.AddField(
            model_name='paymentoption',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.PaymentOptionStatus'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.Profile'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.NominationStatus'),
        ),
        migrations.AddField(
            model_name='itemextra',
            name='product_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductItem'),
        ),
        migrations.AddField(
            model_name='itemextra',
            name='product_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enrollmenttype',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductItem'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrollment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.EnrollmentType'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='gateway_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.GatewayProfile'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.EnrollmentStatus'),
        ),
    ]
