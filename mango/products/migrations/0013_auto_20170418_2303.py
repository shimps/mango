# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170418_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoclaim',
            name='date_of_accident',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='dob_of_driver',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='license_expiry_date',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='o_insurance_end_date',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='o_insurance_start_date',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='registration_date',
            field=models.DateField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
