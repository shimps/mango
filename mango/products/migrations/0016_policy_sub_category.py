# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170419_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='sub_category',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
