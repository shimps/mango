# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_auto_20170413_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('individual', models.BooleanField(default=False)),
                ('company', models.BooleanField(default=False)),
                ('insurance_provider', models.BooleanField(default=False)),
                ('medical_institution', models.BooleanField(default=True)),
                ('police_station', models.BooleanField(default=True)),
                ('service_agent', models.BooleanField(default=True)),
                ('user', models.OneToOneField(related_name='account_type', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
