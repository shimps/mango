# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20170420_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileattachment',
            name='attachment',
            field=models.FileField(null=True, upload_to=products.models.get_upload_file_name, blank=True),
        ),
    ]
