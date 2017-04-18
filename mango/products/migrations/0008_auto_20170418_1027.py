# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170418_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_cover', models.CharField(blank=True, max_length=3, null=True, choices=[(b'PKG', b'Package'), (b'FO', b'Fire Only'), (b'TO', b'Theft Only'), (b'LO', b'Liability Only'), (b'FT', b'Fire and Theft Only'), (b'FL', b'Fire and Liability Only'), (b'TL', b'Theft and Liability Only')])),
                ('vehicle_condition', models.CharField(blank=True, max_length=3, null=True, choices=[(b'OO', b'Original Owner'), (b'SH', b'Second Hand')])),
                ('make', models.CharField(max_length=100, null=True, blank=True)),
                ('model', models.CharField(max_length=100, null=True, blank=True)),
                ('seating_capacity', models.CharField(max_length=3, null=True, blank=True)),
                ('vehicle_usage_area', models.CharField(blank=True, max_length=3, null=True, choices=[(b'U', b'Urban'), (b'R', b'Rural')])),
                ('vehicle_usage_type', models.CharField(blank=True, max_length=3, null=True, choices=[(b'P', b'Private / Social'), (b'D', b'Driving Tuitions'), (b'T', b'Towing')])),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='auto_insurance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='city',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='country',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='email_address',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='income',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'L1K', b'< ZMW1000'), (b'B1K10K', b'ZMW 1000 - 10000'), (b'G1K', b'> ZMW 10000')]),
        ),
        migrations.AddField(
            model_name='application',
            name='income_specify',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='pobox',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='telephone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='title',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'MR', b'Mr'), (b'MRS', b'Mrs'), (b'MS', b'Ms')]),
        ),
        migrations.AddField(
            model_name='autoapplication',
            name='application',
            field=models.OneToOneField(related_name='auto_application', to='products.Application'),
        ),
    ]
