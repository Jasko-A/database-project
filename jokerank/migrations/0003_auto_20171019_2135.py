# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0002_auto_20171018_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_joke_category',
            field=models.CharField(blank=True, max_length=100, choices=[(b'medicine', b'Medicine/Doctor'), (b'politics', b'Politics'), (b'programming', b'Programming'), (b'sports', b'Sports'), (b'children', b'Children'), (b'school', b'School'), (b'animal', b'Animal'), (b'lawyer', b'Lawyer'), (b'math', b'Math'), (b'nerd', b'Nerd'), (b'chuck_norris', b'Chuck Norris')]),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_joke_type1',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue')]),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_joke_type2',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue')]),
        ),
        migrations.AddField(
            model_name='user',
            name='pref_joke_type3',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue')]),
        ),
    ]
