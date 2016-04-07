# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GzipFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipfile', models.FileField(upload_to=b'data')),
            ],
        ),
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
                ('sourcepath', models.ForeignKey(to='bike_status.GzipFile', null=True)),
            ],
        ),
    ]
