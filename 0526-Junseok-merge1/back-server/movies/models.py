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
    backdrop_path = models.CharField(max_length=200, null=True)
    original_language = models.CharField(max_length=100, null=True)

    runtime = models.IntegerField(null=True)
    tagline = models.CharField(max_length=200, null=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    actors = models.ManyToManyField(Actor)
    director_id = models.CharField(max_length=100)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)