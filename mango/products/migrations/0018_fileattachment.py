# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20170418_1558'),
        ('products', '0017_auto_20170420_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_object', models.FileField(null=True, upload_to=b'', blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('application', models.ForeignKey(related_name='files', blank=True, to='products.Application', null=True)),
                ('claim', models.ForeignKey(related_name='files', blank=True, to='products.Claim', null=True)),
                ('medical_institution', models.ForeignKey(related_name='verification_list', blank=True, to='accounts.MedicalAgentAccount', null=True)),
                ('police_station', models.ForeignKey(related_name='verification_list', blank=True, to='accounts.PoliceAgentAccount', null=True)),
                ('service_agent', models.ForeignKey(related_name='verification_list', blank=True, to='accounts.ServiceAgentAccount', null=True)),
            ],
        ),
    ]
