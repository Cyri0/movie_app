from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release = models.DateField()
    poster_image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    average_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
