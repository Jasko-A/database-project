# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0006_auto_20171019_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_nsfw',
            field=models.BooleanField(default=False),
        ),
    ]
