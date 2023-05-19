from django.urls import path
from movies import views

urlpatterns = [
    path('tmdb2/', views.tmdb_data),                            # TMDB 데이터 불러오는 경로
    
    path('movies/top_rated/', views.top_rated_simple_list),         # 최고 평점 기준(18개)
    path('movies/target_month/', views.target_month_simple_list),   # 오늘 날짜 기준(18개)

    path('movies/<int:movie_id>/', views.movie_detail),             # 영화 상세 페이지 정보
    path('movies/<int:movie_id>/actors/', views.get_movie_actors),  # 영화 credits 정보
    
    path('articles/', views.articles_list),                          # 게시글 전체 조회
    path('articles/<int:article_pk>/', views.article_detail),        # 게시글 상세 조회 & 수정 & 삭제
    path('articles/<int:movie_pk>/create/', views.articles_create),  # 게시글 생성
    
    path('movies/comments/', views.movie_comments_list),    # 영화 한줄평 전체 조회
    path('movies/comments/<int:movie_pk>/comments', views.movie_comments_create),    # 영화 한줄평 전체 조회

    # path('movies/', views.movie_list),    # 테스트 url
]
