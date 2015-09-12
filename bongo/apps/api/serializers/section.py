from bongo.apps.bongo import models
from rest_framework import serializers


class SectionSerializer(serializers.ModelSerializer):
    classname = serializers.ReadOnlyField()

    class Meta:
        model = models.Section
        fields = ('id', 'section', 'classname', 'priority')
