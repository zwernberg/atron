# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_league'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.IntegerField(choices=[(0, 'QB'), (1, 'RB'), (2, 'WR'), (3, 'K'), (4, 'TE')]),
        ),
    ]
