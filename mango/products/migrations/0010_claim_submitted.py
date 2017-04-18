# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170418_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
