# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_fileattachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileattachment',
            old_name='file_object',
            new_name='attachment',
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='file_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
