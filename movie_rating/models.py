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

class Rating(models.Model):
    choices = [ (1,1), (2,2), (3,3), (4,4), (5,5) ]
    value = models.IntegerField(choices=choices)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)