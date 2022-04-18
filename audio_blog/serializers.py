from rest_framework import serializers
from .models import StudioAudio


class StudioAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioAudio
        fields = ['id', 'artist', 'title', 'genre', 'poster', 'availability', 'views', 'audio_link', 'slug',
                  'date_posted']
