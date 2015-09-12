from bongo.apps.bongo import models
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'tag',)
