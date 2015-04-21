from bongo.apps.bongo import models
from rest_framework import serializers

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertiser
        fields = ('id', 'name',)