from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_all_movies),
    path('movie/<str:slug>/', views.movie_detail),
    path('movies/action/', views.get_action),
    path('movies/comedy/', views.get_comedy),
    path('movies/television/', views.get_television),
    path('movies/documentary/', views.get_documentary),
    path('movies/drama/', views.get_drama),
    path('movies/family/', views.get_family),
    path('gallery/', views.get_all_gallery),
    path('movies/now_available/', views.get_now_available),
    path('movies/in_theaters/', views.get_in_theaters),
    path('movies/coming_soon/', views.get_coming_soon),
]
