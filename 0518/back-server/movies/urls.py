from django.urls import path
from movies import views

urlpatterns = [
    path('tmdb2/', views.tmdb_data),
    path('movies/', views.movie_list),
]
