# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171019_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='nsfw',
        ),
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.CharField(choices=[('medicine', 'Medicine/Doctor'), ('politics', 'Politics'), ('programming', 'Programming'), ('sports', 'Sports'), ('children', 'Children'), ('school', 'School'), ('animal', 'Animal'), ('lawyer', 'Lawyer'), ('math', 'Math'), ('nerd', 'Nerd'), ('chuck_norris', 'Chuck Norris'), ('dad', 'Dad')], max_length=100),
        ),
        migrations.AlterField(
            model_name='joke',
            name='joke_length',
            field=models.CharField(choices=[('short', 'Short'), ('medium', 'Medium'), ('long', 'Long')], default='short', max_length=100),
        ),
        migrations.AlterField(
            model_name='joke',
            name='joke_type',
            field=models.CharField(choices=[('question', 'Question'), ('pun', 'Pun'), ('one-liner', 'One-Liner'), ('dialogue', 'Dialogue'), ('pickup_line', 'Pick Up Line'), ('punch_line', 'Punch line'), ('fun_fact', 'Fun Fact'), ('other', 'Other')], max_length=100),
        ),
        migrations.AlterModelTable(
            name='joke',
            table='Joke',
        ),
        migrations.AlterModelTable(
            name='jokerating',
            table='JokeRating',
        ),
    ]
