# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20170411_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalAgentAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(default=b'H', max_length=1, choices=[(b'C', b'Clinic'), (b'H', b'Hospital'), (b'O', b'Other')])),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=accounts.models.get_upload_file_name, blank=True)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('pobox', models.CharField(max_length=50, null=True, blank=True)),
                ('province', models.CharField(blank=True, max_length=3, null=True, choices=[(b'COP', b'Copperbelt'), (b'LUS', b'Lusaka'), (b'CEN', b'Central'), (b'NWE', b'North Western'), (b'EAS', b'Eastern'), (b'LUA', b'Luapula'), (b'NOR', b'Northern'), (b'MUC', b'Muchinga'), (b'SOU', b'Southern'), (b'WES', b'Western')])),
                ('country', models.CharField(default=b'ZM', max_length=2, null=True, blank=True, choices=[(b'ZM', b'Zambia')])),
                ('user', models.OneToOneField(related_name='medical_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceAgentAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=accounts.models.get_upload_file_name, blank=True)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('pobox', models.CharField(max_length=50, null=True, blank=True)),
                ('province', models.CharField(blank=True, max_length=3, null=True, choices=[(b'COP', b'Copperbelt'), (b'LUS', b'Lusaka'), (b'CEN', b'Central'), (b'NWE', b'North Western'), (b'EAS', b'Eastern'), (b'LUA', b'Luapula'), (b'NOR', b'Northern'), (b'MUC', b'Muchinga'), (b'SOU', b'Southern'), (b'WES', b'Western')])),
                ('country', models.CharField(default=b'ZM', max_length=2, null=True, blank=True, choices=[(b'ZM', b'Zambia')])),
                ('user', models.OneToOneField(related_name='police_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAgentAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=accounts.models.get_upload_file_name, blank=True)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('pobox', models.CharField(max_length=50, null=True, blank=True)),
                ('province', models.CharField(blank=True, max_length=3, null=True, choices=[(b'COP', b'Copperbelt'), (b'LUS', b'Lusaka'), (b'CEN', b'Central'), (b'NWE', b'North Western'), (b'EAS', b'Eastern'), (b'LUA', b'Luapula'), (b'NOR', b'Northern'), (b'MUC', b'Muchinga'), (b'SOU', b'Southern'), (b'WES', b'Western')])),
                ('country', models.CharField(default=b'ZM', max_length=2, null=True, blank=True, choices=[(b'ZM', b'Zambia')])),
                ('user', models.OneToOneField(related_name='service_agent_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
