# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0008_auto_20151209_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sbi_his', models.CommaSeparatedIntegerField(max_length=3000)),
                ('sno', models.ForeignKey(to='bike_status.Station', null=True)),
            ],
        ),
    ]
