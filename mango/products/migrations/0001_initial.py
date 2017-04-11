# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monthly_cost', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_cover', models.FloatField(default=0)),
                ('coinsurance', models.IntegerField(default=0)),
                ('deductible', models.FloatField(default=0)),
                ('monthly_cost', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='extras',
            name='policy',
            field=models.ForeignKey(related_name='extras', to='products.Policy'),
        ),
    ]
