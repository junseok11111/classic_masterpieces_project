from django.urls import path
from movies import views

urlpatterns = [
    path('tmdb2/', views.tmdb_data),                            # TMDB 데이터 불러오는 경로
    
    path('movies/top_rated/', views.top_rated_simple_list),         # 최고 평점 기준(18개)
    path('movies/target_month/', views.target_month_simple_list),   # 오늘 날짜 기준(18개)

    path('movies/<int:movie_id>/', views.movie_detail),             # 영화 상세 페이지 정보
    path('movies/<int:movie_id>/actors/', views.get_movie_actors),    # 영화 credits 정보
    # path('movies/', views.movie_list),    # 테스트 url
]
