from bongo.apps.bongo import models
from rest_framework import serializers

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PDF
        fields = ('id', 'creators', 'caption', 'staticfile')