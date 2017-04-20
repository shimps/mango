# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_policy_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='sub_category',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'PV', b'Private Vehicle'), (b'CV', b'Commercial Vehicle'), (b'BT', b'Bus/Taxi')]),
        ),
    ]
