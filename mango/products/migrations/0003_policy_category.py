# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170411_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='category',
            field=models.CharField(default='', max_length=3, choices=[(b'H', b'Health'), (b'M', b'Motor'), (b'P', b'Property'), (b'T', b'Travel'), (b'C', b'Commercial')]),
            preserve_default=False,
        ),
    ]
