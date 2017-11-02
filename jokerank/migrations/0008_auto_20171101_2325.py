# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0007_user_show_nsfw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(choices=[('american_indian_alaskan', 'American Indian or Alaska Native'), ('asian', 'Asian'), ('black_or_african_american', 'Black or African American'), ('hawaiian_or_pacific_islander', 'Hawaiian or Other Pacific Islander'), ('white', 'White')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_category',
            field=models.CharField(choices=[('medicine', 'Medicine/Doctor'), ('politics', 'Politics'), ('programming', 'Programming'), ('sports', 'Sports'), ('children', 'Children'), ('school', 'School'), ('animal', 'Animal'), ('lawyer', 'Lawyer'), ('math', 'Math'), ('nerd', 'Nerd'), ('chuck_norris', 'Chuck Norris'), ('dad', 'Dad')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type1',
            field=models.CharField(choices=[('question', 'Question'), ('pun', 'Pun'), ('one-liner', 'One-Liner'), ('dialogue', 'Dialogue'), ('pickup_line', 'Pick Up Line'), ('punch_line', 'Punch line'), ('fun_fact', 'Fun Fact'), ('other', 'Other')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type2',
            field=models.CharField(choices=[('question', 'Question'), ('pun', 'Pun'), ('one-liner', 'One-Liner'), ('dialogue', 'Dialogue'), ('pickup_line', 'Pick Up Line'), ('punch_line', 'Punch line'), ('fun_fact', 'Fun Fact'), ('other', 'Other')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_joke_type3',
            field=models.CharField(choices=[('question', 'Question'), ('pun', 'Pun'), ('one-liner', 'One-Liner'), ('dialogue', 'Dialogue'), ('pickup_line', 'Pick Up Line'), ('punch_line', 'Punch line'), ('fun_fact', 'Fun Fact'), ('other', 'Other')], blank=True, max_length=100),
        ),
    ]
