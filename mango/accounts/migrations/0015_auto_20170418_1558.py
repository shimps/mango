# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_accounttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='medical_institution',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='police_station',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='service_agent',
            field=models.BooleanField(default=False),
        ),
    ]
