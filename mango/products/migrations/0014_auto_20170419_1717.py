# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20170418_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='claim',
            name='decision',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='claim',
            name='declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='income',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'L1K', b'< ZMW1000'), (b'B1K10K', b'ZMW 1000 - 10000'), (b'G10K', b'> ZMW 10000')]),
        ),
    ]
