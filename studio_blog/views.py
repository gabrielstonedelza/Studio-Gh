from django.shortcuts import get_object_or_404
from datetime import datetime, date, time, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import StudioMovies
from .serializers import StudioMoviesSerializer


@api_view(['GET'])
def get_all_movies(request):
    movies = StudioMovies.objects.all().order_by('-date_posted')
    serializer = StudioMoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, slug):
    movie = get_object_or_404(StudioMovies, slug=slug)
    if movie:
        movie.views += 1
        movie.save()
    serializer = StudioMoviesSerializer(movie, many=False)
    return Response(serializer.data)


# get movies by genre
@api_view(['GET'])
def get_action(request):
    action = StudioMovies.objects.filter(genre="Action").order_by('-date_posted')
    serializer = StudioMoviesSerializer(action, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_comedy(request):
    comedy = StudioMovies.objects.filter(genre="Comedy").order_by('-date_posted')
    serializer = StudioMoviesSerializer(comedy, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_documentary(request):
    documentary = StudioMovies.objects.filter(genre="Documentary").order_by('-date_posted')
    serializer = StudioMoviesSerializer(documentary, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_drama(request):
    drama = StudioMovies.objects.filter(genre="Drama").order_by('-date_posted')
    serializer = StudioMoviesSerializer(drama, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_family(request):
    family = StudioMovies.objects.filter(genre="Drama").order_by('-date_posted')
    serializer = StudioMoviesSerializer(family, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_now_available(request):
    now_available = StudioMovies.objects.filter(availability="Now Available").order_by('-date_posted')
    serializer = StudioMoviesSerializer(now_available, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_in_theaters(request):
    in_theaters = StudioMovies.objects.filter(availability="In Theaters").order_by('-date_posted')
    serializer = StudioMoviesSerializer(in_theaters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_coming_soon(request):
    now_available = StudioMovies.objects.filter(availability="Coming Soon").order_by('-date_posted')
    serializer = StudioMoviesSerializer(now_available, many=True)
    return Response(serializer.data)
