# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171101_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='JokeRater',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('joke_submitter_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('birth_country', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('preferred_joke_genre', models.CharField(max_length=100)),
                ('preferred_joke_genre2', models.CharField(blank=True, max_length=100)),
                ('preferred_joke_type', models.CharField(blank=True, max_length=100)),
                ('favorite_music_genre', models.CharField(max_length=100)),
                ('favorite_movie_genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='joke',
            name='joke_length',
        ),
        migrations.RemoveField(
            model_name='jokerating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='jokerating',
            name='would_recommend',
        ),
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='joke',
            name='joke_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jokerating',
            name='joke',
            field=models.ForeignKey(blank=True, related_name='joke_ratings', to='api.Joke', null=True),
        ),
        migrations.AlterField(
            model_name='jokerating',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='joke',
            name='joke_submitter',
            field=models.ForeignKey(blank=True, related_name='jokes_submitted', to='api.JokeRater', null=True),
        ),
        migrations.AddField(
            model_name='jokerating',
            name='joke_rater',
            field=models.ForeignKey(blank=True, related_name='user_ratings', to='api.JokeRater', null=True),
        ),
    ]
