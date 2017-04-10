# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170411_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
    ]
