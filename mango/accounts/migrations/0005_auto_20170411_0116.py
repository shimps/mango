# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_clientaccount_mango_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaccount',
            name='gender',
            field=models.CharField(max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
