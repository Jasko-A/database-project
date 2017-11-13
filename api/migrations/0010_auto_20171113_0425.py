# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171102_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokerater',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
