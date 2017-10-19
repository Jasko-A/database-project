# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0005_user_ethnicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pref_joke_category',
            field=models.CharField(blank=True, max_length=100, choices=[(b'medicine', b'Medicine/Doctor'), (b'politics', b'Politics'), (b'programming', b'Programming'), (b'sports', b'Sports'), (b'children', b'Children'), (b'school', b'School'), (b'animal', b'Animal'), (b'lawyer', b'Lawyer'), (b'math', b'Math'), (b'nerd', b'Nerd'), (b'chuck_norris', b'Chuck Norris'), (b'dad', b'Dad')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type1',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue'), (b'pickup_line', b'Pick Up Line'), (b'punch_line', b'Punch line'), (b'fun_fact', b'Fun Fact'), (b'other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type2',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue'), (b'pickup_line', b'Pick Up Line'), (b'punch_line', b'Punch line'), (b'fun_fact', b'Fun Fact'), (b'other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type3',
            field=models.CharField(blank=True, max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue'), (b'pickup_line', b'Pick Up Line'), (b'punch_line', b'Punch line'), (b'fun_fact', b'Fun Fact'), (b'other', b'Other')]),
        ),
    ]
