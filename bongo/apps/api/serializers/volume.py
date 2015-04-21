from bongo.apps.bongo import models
from rest_framework import serializers

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Volume
        fields = ('id', 'volume_number', 'volume_year_start', 'volume_year_end')