# Generated by Django 4.2.5 on 2024-01-04 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating', '0002_alter_movie_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(blank=True, default=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
