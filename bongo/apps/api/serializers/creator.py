from bongo.apps.bongo import models
from rest_framework import serializers

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Creator
        fields = ('id', 'user', 'name', 'job', 'twitter', 'profpic', 'courtesyof')