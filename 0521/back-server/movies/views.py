from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
import requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer

from .models import Article, MovieComment, ArticleComment
from .serializers import ArticleSerializer, MovieCommentSerializer, ArticleCommentSerializer

from datetime import datetime



##--------- Vue / DB 요청 ---------##
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def top_rated_simple_list(request):
    movies = Movie.objects.order_by('-vote_average')[:18]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def target_month_simple_list(request):
    target_month = datetime.now().month
    movies = Movie.objects.filter(release_date__month=target_month).order_by('-vote_average')
    if len(movies) > 18:
        movies = movies[:18]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie_actors(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    actors = movie.actors.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


##--------- 영화 게시판 ---------##
# 전체 게시글 조회(GET)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articles_list(request):
    articles = get_list_or_404(Article)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
    
# 게시글 생성(POST)
@api_view(['POST'])
def articles_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    print(movie)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시글 상세 조회 & 수정 & 삭제
@api_view(['GET', 'PUT','DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':         # 게시글 상세 조회
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':       # 게시글 수정
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':    # 게시글 삭제
        article.delete()
        msg = f"{article_pk}가 지워졌습니다."
        return Response(msg, status=status.HTTP_204_NO_CONTENT)


##---------- 영화 한줄평  ----------##
@api_view(['GET', 'POST'])
def movie_comments_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    # 영화 한줄평 전체 조회
    if request.method == 'GET':
        movie_comments = MovieComment.objects.filter(movie_id=movie_pk)
        serializer = MovieCommentSerializer(movie_comments, many=True)
        return Response(serializer.data)
    
    # 영화 한줄평 생성
    elif request.method == 'POST':
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    

# 영화 한줄평 조회 & 수정 & 삭제
@api_view(['GET', 'PUT','DELETE'])
def movie_comments_detail(request, movie_pk, comment_pk):
    movie_comment = MovieComment.objects.filter(movie_id=movie_pk).get(pk=comment_pk)
    
    if request.method == 'PUT':       # 영화 한줄평 수정
        serializer = MovieCommentSerializer(movie_comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':    # 영화 한줄평 삭제
        movie_comment.delete()
        msg = f"영화 id: {movie_pk}의 댓글 id: {comment_pk}가 지워졌습니다."
        return Response(msg, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':         # 영화 한줄평 상세 조회 (테스트용)
        serializer = MovieCommentSerializer(movie_comment)
        return Response(serializer.data)


##---------- 영화 게시판 댓글  ----------##
# 영화 게시판 댓글 생성
@api_view(['POST'])
def article_comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)

# 영화 게시판 댓글 조회 & 수정 & 삭제
@api_view(['GET', 'PUT','DELETE'])
def article_comments_detail(request, article_pk, comment_pk):
    article_comment = ArticleComment.objects.filter(article_id=article_pk).get(pk=comment_pk)
    
    if request.method == 'PUT':       # 영화 게시판 댓글 수정
        serializer = ArticleCommentSerializer(article_comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':    # 영화 게시판 댓글 삭제
        article_comment.delete()
        msg = f"게시글 id: {article_pk}의 댓글 id: {comment_pk}가 지워졌습니다."
        return Response(msg, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':         # 영화 게시판 댓글 상세 조회 (테스트용)
        serializer = ArticleCommentSerializer(article_comment)
        return Response(serializer.data)















# TMDB API KEY 작성
API_KEY = '495188919e47c75e31092046a89fe473'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
DISCOVER_MOVIE_URL = 'https://api.themoviedb.org/3/discover/movie'

def tmdb_genres():  # TMDB -> Django DB 장르 데이터
    # TMDB에서 Genre 데이터 가져오기
    # https://developer.themoviedb.org/reference/genre-movie-list
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        # Genre 모델의 pk와 일치하는 genre['id']가 있으면 continue
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        print(genre)
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)

def get_youtube_key(movie_dict): # TMDB -> Django DB youtube key   
    movie_id = movie_dict.get('id')

    # TMDB에서 youtube key 가져오기
    # https://developer.themoviedb.org/reference/movie-videos
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_person(person_id):
    # TMDB에서 년도별 데이터 받아오기
    # https://developer.themoviedb.org/reference/person-details
    response = requests.get(
        f'https://api.themoviedb.org/3/person/{person_id}',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    return response

def get_credits(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()

    # 해당 영화에 출연한 배우들 정보 가져오기
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        person_id = person.get('id')

        if not Actor.objects.filter(pk=person_id).exists():
            actor_data = get_person(person_id)
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name'),
                profile_path=person.get('profile_path'),
                birthday=actor_data.get('birthday'),
                deathday=actor_data.get('deathday')
            )
        movie.actors.add(person_id)
        if movie.actors.count() == 5:
            break
    
    # 해당 영화의 감독 정보 가져오기
    for person in response.get('crew'):
        if person.get('job') != 'Director': continue
        person_id = person.get('id')

        if not Director.objects.filter(pk=person_id).exists():
            director_data = get_person(person_id)
            director = Director.objects.create(
                id=person.get('id'),
                name=person.get('name'),
                profile_path=person.get('profile_path'),
                birthday=director_data.get('birthday'),
                deathday=director_data.get('deathday')
            )
            movie.director_id = person.get('id')
            movie.save()
        return person_id

def movie_data(year=1980, page=1):
    # TMDB에서 년도별 데이터 받아오기
    # https://developer.themoviedb.org/reference/discover-movie
    response = requests.get(
    DISCOVER_MOVIE_URL,
    params = {
        'api_key': API_KEY,
        'include_adult': 'false',
        'include_video': 'false',
        'language': 'ko-kr',
        'page': page,
        'primary_release_year': year,
        'sort_by': {'vote_count.desc', 'vote_average.desc'}
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        if int(movie_dict.get('vote_average')) < 5 : continue   # 없는 필드 skip
        if not movie_dict.get('overview'): continue   # 없는 필드 skip
        if not movie_dict.get('poster_path'): continue   # 없는 필드 skip
        
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)

        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key,
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 감독, 배우들 저장
        get_credits(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)

def tmdb_data(request):
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Movie.objects.all().delete()

    tmdb_genres()
    for i in range(1980, 2000):
        for j in range(1, 3):
            movie_data(i, j)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

