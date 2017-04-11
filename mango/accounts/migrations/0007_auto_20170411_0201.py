# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_clientaccount_nrc'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('pobox', models.CharField(max_length=50, null=True, blank=True)),
                ('province', models.CharField(blank=True, max_length=3, null=True, choices=[(b'COP', b'Copperbelt'), (b'LUS', b'Lusaka'), (b'CEN', b'Central'), (b'NWE', b'North Western'), (b'EAS', b'Eastern'), (b'LUA', b'Luapula'), (b'NOR', b'Northern'), (b'MUC', b'Muchinga'), (b'SOU', b'Southern'), (b'WES', b'Western')])),
                ('country', models.CharField(default=b'ZM', max_length=2, null=True, blank=True, choices=[(b'ZM', b'Zambia')])),
            ],
        ),
        migrations.AddField(
            model_name='clientaccount',
            name='pobox',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='mango_id',
            field=models.CharField(default=b'p10000', max_length=20, unique=True, null=True, blank=True),
        ),
    ]
