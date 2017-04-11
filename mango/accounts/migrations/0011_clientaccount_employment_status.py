# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_mangoagent'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='employment_status',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'E', b'Employed'), (b'U', b'Unemployed'), (b'S', b'Self Employed / Contractor')]),
        ),
    ]
