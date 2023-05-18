from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer

from datetime import datetime

@api_view(['GET'])
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



# @api_view(['GET'])
# def movie_list(request):
#     movies = get_list_or_404(Movie)[:18]
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)









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

