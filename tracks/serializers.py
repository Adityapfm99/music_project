from rest_framework import serializers
from .models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'file', 'artist', 'title')
        extra_kwargs = {
                    'id': {'read_only': True},
                    'file': {'required': False},
                    'artist': {'required': False},  
                    'title': {'required': False},   
                }