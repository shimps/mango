# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20170411_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='image',
            field=models.FileField(null=True, upload_to=accounts.models.get_upload_file_name, blank=True),
        ),
        migrations.AddField(
            model_name='companyaccount',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyaccount',
            name='image',
            field=models.FileField(null=True, upload_to=accounts.models.get_upload_file_name, blank=True),
        ),
        migrations.AddField(
            model_name='companyaccount',
            name='mango_id',
            field=models.CharField(default=b'c10000', max_length=20, unique=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyaccount',
            name='user',
            field=models.OneToOneField(related_name='company_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='user',
            field=models.OneToOneField(related_name='client_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
