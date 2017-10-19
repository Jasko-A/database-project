# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0004_remove_user_ethnicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=100, choices=[(b'american_indian_alaskan', b'American Indian or Alaska Native'), (b'asian', b'Asian'), (b'black_or_african_american', b'Black or African American'), (b'hawaiian_or_pacific_islander', b'Hawaiian or Other Pacific Islander'), (b'white', b'White')]),
        ),
    ]
