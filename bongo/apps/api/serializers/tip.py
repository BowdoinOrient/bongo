from bongo.apps.bongo import models
from rest_framework import serializers

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tip
        fields = ('id', 'content', 'respond_to', 'submitted_at', 'submitted_from', 'useragent')