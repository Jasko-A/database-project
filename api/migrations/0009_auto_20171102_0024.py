# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_joke_joke_source'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='jokerater',
            table='JokeRater',
        ),
    ]
