# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20171113_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokerater',
            name='birth_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='jokerater',
            name='preferred_joke_genre2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jokerater',
            name='preferred_joke_type',
            field=models.CharField(max_length=100),
        ),
    ]
