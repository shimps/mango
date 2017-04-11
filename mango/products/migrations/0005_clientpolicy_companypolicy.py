# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_insurancecompanyaccount'),
        ('products', '0004_auto_20170411_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('cancel_date', models.DateTimeField(null=True, blank=True)),
                ('client', models.ForeignKey(related_name='clients', to='accounts.ClientAccount')),
                ('policy', models.ForeignKey(related_name='client_policies', to='products.Policy')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('cancel_date', models.DateTimeField(null=True, blank=True)),
                ('company', models.ForeignKey(related_name='companies', to='accounts.CompanyAccount')),
                ('policy', models.ForeignKey(related_name='company_policies', to='products.Policy')),
            ],
        ),
    ]
