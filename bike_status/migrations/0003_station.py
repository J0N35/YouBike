# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0002_auto_20151208_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('sno', models.IntegerField(serialize=False, primary_key=True)),
                ('sna', models.TextField()),
                ('tot', models.IntegerField()),
                ('sbi', models.IntegerField()),
                ('sarea', models.TextField()),
                ('mday', models.DateTimeField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('ar', models.TextField()),
                ('sareaen', models.TextField()),
                ('snaen', models.TextField()),
                ('aren', models.TextField()),
                ('bemp', models.IntegerField()),
                ('act', models.BooleanField()),
                ('source_path', models.ForeignKey(to='bike_status.GzipFile', null=True)),
            ],
        ),
    ]
