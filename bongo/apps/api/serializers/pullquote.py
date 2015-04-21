from bongo.apps.bongo import models
from rest_framework import serializers

class PullquoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pullquote
        fields = ('id', 'creators', 'caption', 'quote', 'attribution')