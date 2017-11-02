# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171101_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='joke_source',
            field=models.CharField(default='00', max_length=100),
            preserve_default=False,
        ),
    ]
