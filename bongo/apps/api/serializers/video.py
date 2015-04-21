from bongo.apps.bongo import models
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('id', 'creators', 'caption', 'host', 'uid')