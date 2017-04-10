# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaccount',
            name='title',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'MR', b'Mr'), (b'MRS', b'Mrs'), (b'MS', b'Ms')]),
        ),
    ]
