# Generated by Django 2.0.1 on 2018-01-11 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0007_auto_20180102_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Preseason'), (1, 'In Season'), (2, 'Season Over')])),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='league.Season'),
        ),
        migrations.AddField(
            model_name='league',
            name='season',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='leagues', to='league.Season'),
            preserve_default=False,
        ),
    ]