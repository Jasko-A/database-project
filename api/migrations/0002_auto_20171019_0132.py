# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='word_count',
        ),
        migrations.AddField(
            model_name='joke',
            name='joke_length',
            field=models.CharField(default=b'short', max_length=100, choices=[(b'short', b'Short'), (b'medium', b'Medium'), (b'long', b'Long')]),
        ),
    ]
