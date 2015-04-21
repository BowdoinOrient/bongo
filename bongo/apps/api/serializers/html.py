from bongo.apps.bongo import models
from rest_framework import serializers

class HTMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HTML
        fields = ('id', 'creators', 'caption', 'content')