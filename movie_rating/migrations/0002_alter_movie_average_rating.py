# Generated by Django 4.2.5 on 2024-01-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(blank=True, default='null', null=True),
        ),
    ]
