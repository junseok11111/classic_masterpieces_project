from rest_framework import serializers
from .models import Movie, Actor, Article, MovieComment, ArticleComment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('movie',)

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie',)