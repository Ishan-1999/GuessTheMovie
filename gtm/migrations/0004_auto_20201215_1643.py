# Generated by Django 3.1 on 2020-12-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtm', '0003_auto_20201207_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='hint1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='hint2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='hint3',
            field=models.CharField(max_length=500),
        ),
    ]