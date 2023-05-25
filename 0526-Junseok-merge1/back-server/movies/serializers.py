from rest_framework import serializers
from .models import Movie, Actor, Article, MovieComment, ArticleComment

# 영화 전체 정보
class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 영화 한줄 평
class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'user_name')

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
        read_only_fields = ('article', 'user', 'user_name')

# 게시글 정보
class ArticleSerializer(serializers.ModelSerializer):
    articlecomment_set = ArticleCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'user_name')

# 영화 검색 정보
class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'poster_path')

# 영화 좋아요한 수 정보
class MovieLikeCountSerializer(serializers.Serializer):
    movie_like_count = serializers.IntegerField()