from bongo.apps.bongo import models
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'title',)
