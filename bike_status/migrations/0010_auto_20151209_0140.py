# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0009_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='sbi_his',
        ),
        migrations.AddField(
            model_name='history',
            name='sbi',
            field=models.IntegerField(null=True),
        ),
    ]
