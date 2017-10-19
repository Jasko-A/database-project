# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokerank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_country',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=100, choices=[(b'male', b'Male'), (b'female', b'Female'), (b'other', b'Other')]),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
