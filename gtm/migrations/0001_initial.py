# Generated by Django 3.1 on 2020-12-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('hint1', models.CharField(max_length=50)),
                ('hint2', models.CharField(max_length=50)),
                ('hint3', models.CharField(max_length=50)),
            ],
        ),
    ]