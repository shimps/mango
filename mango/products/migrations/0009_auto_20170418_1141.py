# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170418_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='income_specify',
            new_name='funding_specify',
        ),
        migrations.AddField(
            model_name='application',
            name='funding_sources',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'S', b'Salary'), (b'B', b'Business'), (b'O', b'Other')]),
        ),
    ]
