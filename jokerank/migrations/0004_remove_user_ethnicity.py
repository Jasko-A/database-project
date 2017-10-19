# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0003_auto_20171019_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ethnicity',
        ),
    ]
