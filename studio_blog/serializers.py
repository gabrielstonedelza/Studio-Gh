from rest_framework import serializers
from .models import StudioMovies


class StudioMoviesSerializer(serializers.ModletSerializer):
    class Meta:
        model = StudioMovies
        fields = ['id', 'movie_title', 'genre', 'poster', 'availability', 'views', 'description', 'movie_link', 'slug',
                  'date_posted']
