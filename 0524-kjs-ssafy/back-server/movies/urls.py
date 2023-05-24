from django.urls import path
from movies import views

urlpatterns = [
    path('tmdb2/', views.tmdb_data),                            # TMDB 데이터 불러오는 경로
    
    path('movies/top_rated/', views.top_rated_simple_list),         # 최고 평점 기준(18개)
    path('movies/target_month/', views.target_month_simple_list),   # 오늘 날짜 기준(18개)

    # ---영화 상세 페이지---
    path('movies/<int:movie_id>/', views.movie_detail),             # 영화 상세 페이지 정보
    path('movies/<int:movie_id>/actors/', views.get_movie_actors),  # 영화 credits 정보
    
    # ---영화 게시글---
    path('articles/', views.articles_list_or_create),                # 게시글 전체 조회 & 생성
    path('articles/<int:article_pk>/', views.article_detail),        # 게시글 상세 조회 & 수정 & 삭제
    
    # ---영화 한줄평---
    path('movies/<int:movie_pk>/comments/', views.movie_comments_list_or_create),    # 영화 한줄평 생성 & 전체조회
    path('movies/<int:movie_pk>/comments/<int:comment_pk>/', views.movie_comments_detail), # 영화 한줄평 상세 조회 & 수정 & 삭제

    # ---영화 게시판 댓글---
    path('articles/<int:article_pk>/comments/', views.article_comments_list_or_create),    # 영화 게시판 댓글 생성
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.article_comments_detail), # 영화 게시판 댓글 상세 조회 & 수정 & 삭제

    # --- 영화 좋아요 ---
    path('movies/<int:movie_pk>/movie_likes/', views.movie_likes),

    # --- 영화 검색 ---
    path('movies/search/', views.movie_search),

    # path('movies/', views.movie_list),    # 테스트 url
]
