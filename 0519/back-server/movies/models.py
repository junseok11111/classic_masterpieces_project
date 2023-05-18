from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)

class Director(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200, null=True)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    actors = models.ManyToManyField(Actor)
    director_id = models.CharField(max_length=100)