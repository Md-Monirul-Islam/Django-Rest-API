from django.shortcuts import render
from .models import Song, Singer
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets

# Create your views here.


class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
