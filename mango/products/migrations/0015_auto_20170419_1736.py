# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20170419_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_of_submission',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='date_of_submission',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
