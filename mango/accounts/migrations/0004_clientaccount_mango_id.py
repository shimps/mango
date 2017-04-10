# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_clientaccount_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='mango_id',
            field=models.IntegerField(default=10000, unique=True, null=True, blank=True),
        ),
    ]
