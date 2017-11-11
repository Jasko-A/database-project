# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171102_0024'),
        ('jokerank', '0009_auto_20171110_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joke_rater',
            field=models.OneToOneField(null=True, blank=True, to='api.JokeRater'),
        ),
    ]
