# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=3, null=True, choices=[(b'MR', b'Mr'), (b'MRS', b'mrs'), (b'Ms', b'MS')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=2)),
                ('marital_status', models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'Single'), (b'M', b'Married'), (b'D', b'Divorced'), (b'W', b'Widowed')])),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('province', models.CharField(blank=True, max_length=3, null=True, choices=[(b'COP', b'Copperbelt'), (b'LUS', b'Lusaka'), (b'CEN', b'Central'), (b'NWE', b'North Western'), (b'EAS', b'Eastern'), (b'LUA', b'Luapula'), (b'NOR', b'Northern'), (b'MUC', b'Muchinga'), (b'SOU', b'Southern'), (b'WES', b'Western')])),
                ('country', models.CharField(default=b'ZM', max_length=2, null=True, blank=True, choices=[(b'ZM', b'Zambia')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
