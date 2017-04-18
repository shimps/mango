# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_auto_20170411_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('policy', models.ForeignKey(related_name='policy_applications', to='products.Policy')),
                ('user', models.ForeignKey(related_name='policy_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AutoClaim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_number', models.CharField(max_length=100, null=True, blank=True)),
                ('make', models.CharField(max_length=100, null=True, blank=True)),
                ('model', models.CharField(max_length=100, null=True, blank=True)),
                ('registration_date', models.DateField(null=True, blank=True)),
                ('date_of_accident', models.DateField(null=True, blank=True)),
                ('time_of_accident', models.CharField(max_length=100, null=True, blank=True)),
                ('place_of_accident', models.CharField(max_length=100, null=True, blank=True)),
                ('police_station', models.CharField(max_length=100, null=True, blank=True)),
                ('garage_name', models.CharField(max_length=100, null=True, blank=True)),
                ('loss_estimate', models.CharField(max_length=100, null=True, blank=True)),
                ('number_in_vehicle', models.CharField(max_length=100, null=True, blank=True)),
                ('name_of_driver', models.CharField(max_length=100, null=True, blank=True)),
                ('dob_of_driver', models.DateField(null=True, blank=True)),
                ('license_number', models.CharField(max_length=100, null=True, blank=True)),
                ('license_expiry_date', models.DateField(null=True, blank=True)),
                ('vehicle_authorization', models.CharField(max_length=200, null=True, blank=True)),
                ('o_insurance_company', models.CharField(max_length=200, null=True, blank=True)),
                ('o_insurance_policy_number', models.CharField(max_length=200, null=True, blank=True)),
                ('o_insurance_start_date', models.DateField(null=True, blank=True)),
                ('o_insurance_end_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=3, null=True, choices=[(b'MR', b'Mr'), (b'MRS', b'Mrs'), (b'MS', b'Ms')])),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
                ('pobox', models.CharField(max_length=50, null=True, blank=True)),
                ('telephone', models.CharField(max_length=50, null=True, blank=True)),
                ('email_address', models.CharField(max_length=100, null=True, blank=True)),
                ('payment_method', models.CharField(max_length=100, null=True, blank=True)),
                ('payment_details', models.CharField(max_length=100, null=True, blank=True)),
                ('auto_insurance', models.BooleanField(default=False)),
                ('policy', models.ForeignKey(related_name='policy_claims', to='products.ClientPolicy')),
                ('user', models.ForeignKey(related_name='claims', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='autoclaim',
            name='claim',
            field=models.OneToOneField(related_name='auto_claim', to='products.Claim'),
        ),
    ]
