# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_insurancecompanyaccount'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverageDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CoverageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='policy',
            name='insurance_company',
            field=models.ForeignKey(related_name='policies', blank=True, to='accounts.InsuranceCompanyAccount', null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coveragetype',
            name='policy',
            field=models.ForeignKey(related_name='coverage_types', to='products.Policy'),
        ),
        migrations.AddField(
            model_name='coveragedetail',
            name='coverage_type',
            field=models.ForeignKey(related_name='coverage_details', to='products.CoverageType'),
        ),
    ]
