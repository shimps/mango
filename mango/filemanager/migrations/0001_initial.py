# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filemanager.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file_object', models.FileField(null=True, upload_to=filemanager.models.get_upload_file_name, blank=True)),
                ('user', models.ForeignKey(related_name='files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
