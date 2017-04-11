# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_clientpolicy_companypolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientpolicy',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companypolicy',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
