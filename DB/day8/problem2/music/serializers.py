from rest_framework import serializers
from .models import Music


def MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id','title',)

def MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'