# Generated by Django 3.1 on 2020-12-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('points', models.IntegerField(max_length=50)),
            ],
        ),
    ]