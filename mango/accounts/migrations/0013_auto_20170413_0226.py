# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_insurancecompanyaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyaccount',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='insurancecompanyaccount',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='medicalagentaccount',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='policeagentaccount',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviceagentaccount',
            name='email',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
