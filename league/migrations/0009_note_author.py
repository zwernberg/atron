# Generated by Django 2.0.1 on 2018-01-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0008_auto_20180111_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.CharField(default='Todd Schultz', max_length=100),
            preserve_default=False,
        ),
    ]