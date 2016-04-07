# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0004_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='sna',
        ),
        migrations.AlterField(
            model_name='history',
            name='sbi_his',
            field=models.CommaSeparatedIntegerField(max_length=3000),
        ),
    ]
