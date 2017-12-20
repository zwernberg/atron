# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_team_league_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.CharField(default='DOT', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.IntegerField(choices=[(0, 'QB'), (1, 'RB'), (2, 'WR'), (3, 'K'), (4, 'TE')], max_length=10),
        ),
    ]