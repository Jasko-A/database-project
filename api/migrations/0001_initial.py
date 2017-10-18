# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, choices=[(b'medicine', b'Medicine/Doctor'), (b'politics', b'Politics'), (b'programming', b'Programming'), (b'sports', b'Sports'), (b'children', b'Children'), (b'school', b'School'), (b'animal', b'Animal'), (b'lawyer', b'Lawyer'), (b'math', b'Math'), (b'nerd', b'Nerd'), (b'chuck_norris', b'Chuck Norris')])),
                ('joke_type', models.CharField(max_length=100, choices=[(b'question', b'Question'), (b'pun', b'Pun'), (b'one-liner', b'One-Liner'), (b'dialogue', b'Dialogue')])),
                ('word_count', models.PositiveIntegerField()),
                ('nsfw', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=100)),
                ('joke_text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='JokeRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField()),
                ('would_recommend', models.BooleanField(default=False)),
                ('joke', models.ForeignKey(related_name='joke_ratings', to='api.Joke')),
                ('user', models.ForeignKey(related_name='joke_raters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
