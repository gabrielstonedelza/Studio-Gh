from django.shortcuts import get_object_or_404
from datetime import datetime, date, time, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import StudioAudio
from .serializers import StudioAudioSerializer


@api_view(['GET'])
def get_all_audio(request):
    audios = StudioAudio.objects.all().order_by('-date_posted')
    serializer = StudioAudioSerializer(audios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def audio_detail(request, slug):
    audio = get_object_or_404(StudioAudio, slug=slug)
    if audio:
        audio.views += 1
        audio.save()
    serializer = StudioAudioSerializer(audio, many=False)
    return Response(serializer.data)


# get movies by genre
@api_view(['GET'])
def get_free_style(request):
    free_style = StudioAudio.objects.filter(genre="Free Style").order_by('-date_posted')
    serializer = StudioAudioSerializer(free_style, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_dance_hall(request):
    dance_hall = StudioAudio.objects.filter(genre="Dance Hall").order_by('-date_posted')
    serializer = StudioAudioSerializer(dance_hall, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_gospel(request):
    gospel = StudioAudio.objects.filter(genre="Gospel").order_by('-date_posted')
    serializer = StudioAudioSerializer(gospel, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_jama(request):
    jama = StudioAudio.objects.filter(genre="Jama").order_by('-date_posted')
    serializer = StudioAudioSerializer(jama, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_hip_life(request):
    hip_life = StudioAudio.objects.filter(genre="Hip Life").order_by('-date_posted')
    serializer = StudioAudioSerializer(hip_life, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_adadam(request):
    adadam = StudioAudio.objects.filter(genre="Adadam").order_by('-date_posted')
    serializer = StudioAudioSerializer(adadam, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_on_air(request):
    on_air = StudioAudio.objects.filter(availability="On Air").order_by('-date_posted')
    serializer = StudioAudioSerializer(on_air, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_coming_soon(request):
    coming_soon = StudioAudio.objects.filter(availability="Coming Soon").order_by('-date_posted')
    serializer = StudioAudioSerializer(coming_soon, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_now_available(request):
    now_available = StudioAudio.objects.filter(availability="Now Available").order_by('-date_posted')
    serializer = StudioAudioSerializer(now_available, many=True)
    return Response(serializer.data)
