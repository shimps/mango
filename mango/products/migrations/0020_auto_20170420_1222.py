# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20170420_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='required_documents_application',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='required_documents_claim',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
