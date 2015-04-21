from bongo.apps.bongo import models
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id', )