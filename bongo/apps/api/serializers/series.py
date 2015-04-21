from bongo.apps.bongo import models
from rest_framework import serializers

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Series
        fields = ('id', 'name',)