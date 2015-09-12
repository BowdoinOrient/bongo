from bongo.apps.bongo import models
from rest_framework import serializers


class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScheduledPost
        fields = ('id', )
