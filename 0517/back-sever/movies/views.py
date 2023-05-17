# from django.shortcuts import get_object_or_404, get_list_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Genre, Movie, Actor
import requests

# TMDB API KEY
API_KEY = '495188919e47c75e31092046a89fe473'

GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
DISCOVER_MOVIE_URL = 'https://api.themoviedb.org/3/discover/movie'

# TMDB -> Django DB 장르 데이터
def tmdb_genres():
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
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)

# TMDB -> Django DB youtube key 가져오기
def get_youtube_key(movie_dict):
    movie_id = movie_dict.get('id')

    # TMDB에서 youtube key 가져오기
    # https://developer.themoviedb.org/reference/movie-videos
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'


def movie_data(year=1980, page=1):
    # TMDB에서 년도별 데이터 받아오기
    # https://developer.themoviedb.org/reference/discover-movie
    response = requests.get(
        DISCOVER_MOVIE_URL,
        params = {
            'include_adult': 'false',
            'include_video': 'false',
            'language': 'ko-kr',
            'page': page,
            'primary_release_year': year,
            'sort_by': 'primary_release_date.asc'
            }
        ).json()
    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue # 없는 필드 skip
        if movie_dict.get('vote_average') < 5: continue # 평점 5점 미만 skip

        # 유튜브 key 조회
        youtube_key = get_youtube_key(movie_dict)

        # overview 조회

        movie = Movie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key    
        )

def tmdb_data(request):
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Movie.objects.all().delete()

