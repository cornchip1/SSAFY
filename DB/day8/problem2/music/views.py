from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import HttpResponse


from .serializers import MusicListSerializer, MusicSerializer
from .models import Music

@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        musics = get_list_or_404(Music)
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)