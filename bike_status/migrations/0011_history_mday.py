# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_status', '0010_auto_20151209_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='mday',
            field=models.DateTimeField(null=True),
        ),
    ]
