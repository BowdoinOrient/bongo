from bongo.apps.bongo import models
from rest_framework import serializers


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alert
        fields = ('id', 'run_from', 'run_through', 'message', 'urgent')
