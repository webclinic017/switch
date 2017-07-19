# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-23 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vcs', '0001_initial'),
        ('administration', '0001_initial'),
        ('upc', '0001_initial'),
        ('crm', '0001_initial'),
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('subscription_details', models.CharField(max_length=1920)),
                ('subscribed', models.BooleanField(default=False)),
                ('linkid', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('gateway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Gateway')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='ContactStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('credit_value', models.IntegerField()),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.Institution')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=640)),
                ('account_id', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(max_length=3840)),
                ('inst_notified', models.NullBooleanField(default=False)),
                ('inst_num_tries', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InBoundState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('ext_service_id', models.CharField(max_length=250)),
                ('ext_service_username', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('ext_service_password', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('ext_service_details', models.CharField(blank=True, max_length=1920, null=True)),
                ('institution_url', models.CharField(blank=True, max_length=640, null=True)),
                ('institution_username', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('institution_password', models.CharField(blank=True, help_text=b'Optional', max_length=320, null=True)),
                ('channel', models.ManyToManyField(blank=True, to='administration.Channel')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcs.Code')),
                ('endpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notify.Endpoint')),
                ('institution_till', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upc.InstitutionTill')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge.Service')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('file_path', models.FileField(blank=True, max_length=200, null=True, upload_to=b'notify_notificationattachment_path/')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=100)),
                ('ext_product_id', models.CharField(blank=True, max_length=250, null=True)),
                ('keyword', models.CharField(blank=True, max_length=45, null=True)),
                ('subscribable', models.NullBooleanField(default=False)),
                ('expires', models.NullBooleanField(default=False)),
                ('unit_credit_charge', models.DecimalField(decimal_places=2, max_digits=19)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.Notification')),
                ('payment_method', models.ManyToManyField(blank=True, to='bridge.PaymentMethod')),
                ('product_type', models.ManyToManyField(blank=True, to='crm.ProductType')),
                ('service', models.ManyToManyField(blank=True, to='bridge.Service')),
                ('subscription_endpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notify.Endpoint')),
                ('unsubscription_endpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unsubscription_endpoint', to='notify.Endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('template_heading', models.CharField(max_length=45)),
                ('template_message', models.CharField(max_length=3840)),
                ('description', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(blank=True, to='notify.NotificationProduct')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(max_length=3840)),
                ('scheduled_send', models.DateTimeField()),
                ('sends', models.IntegerField()),
                ('ext_outbound_id', models.CharField(blank=True, max_length=200, null=True)),
                ('inst_notified', models.NullBooleanField(default=False)),
                ('inst_num_tries', models.IntegerField(blank=True, null=True)),
                ('attachment', models.ManyToManyField(blank=True, to='notify.NotificationAttachment')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='OutBoundState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('auto', models.BooleanField(default=False)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='notify.NotificationProduct')),
                ('response_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autoresponse__auto_notification', to='notify.NotificationProduct')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('file_path', models.FileField(blank=True, max_length=200, null=True, upload_to=b'notify_templatefile_path/')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='outbound',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.OutBoundState'),
        ),
        migrations.AddField(
            model_name='outbound',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notify.NotificationTemplate'),
        ),
        migrations.AddField(
            model_name='notificationtemplate',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.TemplateStatus'),
        ),
        migrations.AddField(
            model_name='notificationtemplate',
            name='template_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notify.TemplateFile'),
        ),
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.NotificationStatus'),
        ),
        migrations.AddField(
            model_name='inbound',
            name='attachment',
            field=models.ManyToManyField(blank=True, to='notify.NotificationAttachment'),
        ),
        migrations.AddField(
            model_name='inbound',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.Contact'),
        ),
        migrations.AddField(
            model_name='inbound',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.InBoundState'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_group',
            field=models.ManyToManyField(blank=True, to='notify.ContactGroup'),
        ),
        migrations.AddField(
            model_name='contact',
            name='gateway_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upc.GatewayProfile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.NotificationProduct'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notify.ContactStatus'),
        ),
    ]
