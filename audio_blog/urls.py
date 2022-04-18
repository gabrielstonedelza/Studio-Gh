from django.urls import path

from studio.urls import urlpatterns
from . import views

urlpatterns = [
    path('audios/', views.get_all_audio),
    path('audio/<str:slug>/', views.audio_detail),
    path('audio/free_style/', views.get_free_style),
    path('audio/dance_hall/', views.get_dance_hall),
    path('audio/gospel/', views.get_gospel),
    path('audio/jama/', views.get_jama),
    path('audio/hip_life/', views.get_hip_life),
    path('audio/adadam/', views.get_adadam),
    path('audio/on_air/', views.get_on_air),
    path('audio/coming_soon/', views.get_coming_soon),
    path('audio/now_available/', views.get_now_available),
]