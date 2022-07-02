from rest_framework import serializers
from .models import StudioMovies, Gallery


class StudioMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioMovies
        fields = ['id', 'movie_title', 'genre', 'poster', 'availability', 'views', 'description', 'movie_link', 'slug',
                  'get_movie_poster',
                  'date_posted']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'date_posted']
