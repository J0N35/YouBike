# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0005_auto_20151209_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='sno',
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
