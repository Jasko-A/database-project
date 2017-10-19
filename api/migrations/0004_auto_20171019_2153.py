# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171019_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokerating',
            name='rating',
            field=models.PositiveIntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
