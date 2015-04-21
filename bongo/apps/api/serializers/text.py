from bongo.apps.bongo import models
from rest_framework import serializers

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = ('id', 'creators', 'caption', 'body', 'excerpt')