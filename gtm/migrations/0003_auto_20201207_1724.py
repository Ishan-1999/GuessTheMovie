# Generated by Django 3.1 on 2020-12-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtm', '0002_leaderboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='points',
            field=models.IntegerField(),
        ),
    ]
