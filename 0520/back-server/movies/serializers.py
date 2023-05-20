from rest_framework import serializers
from .models import Movie, Actor, Article, MovieComment, ArticleComment

# 영화 한줄 평
class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('movie',)

# 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):
    moviecomment_set = MovieCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 배우 정보
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 게시글 댓글 정보
class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('article',)

# 게시글 정보
class ArticleSerializer(serializers.ModelSerializer):
    articlecomment_set = ArticleCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie',)