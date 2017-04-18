# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_application_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoclaim',
            name='date_of_accident',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='dob_of_driver',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='o_insurance_end_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='o_insurance_start_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='autoclaim',
            name='registration_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
    ]
