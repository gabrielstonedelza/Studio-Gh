from django.urls import path

from studio.urls import urlpatterns
from . import views

urlpatterns = [
    path('movies/', views.get_all_movies),
    path('movie<str:slug>/', views.movie_detail),
    path('movie/action/', views.get_action),
    path('movie/comedy/', views.get_comedy),
    path('movie/documentary/', views.get_documentary),
    path('movie/drama/', views.get_drama),
    path('movie/family/', views.get_family),
    path('movie/now_available/', views.get_now_available),
    path('movie/in_theaters/', views.get_in_theaters),
    path('movie/coming_soon/', views.get_coming_soon),
]
