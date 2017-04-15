# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200, null=True, blank=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=200)),
                ('receiver', models.ForeignKey(related_name='received_messages', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='sent_messages', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
