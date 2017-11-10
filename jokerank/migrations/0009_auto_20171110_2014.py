# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0008_auto_20171101_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country_of_origin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pref_joke_category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pref_joke_type1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pref_joke_type2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pref_joke_type3',
        ),
        migrations.RemoveField(
            model_name='user',
            name='show_nsfw',
        ),
    ]
