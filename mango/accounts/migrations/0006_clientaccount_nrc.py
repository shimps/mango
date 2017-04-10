# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170411_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='nrc',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
