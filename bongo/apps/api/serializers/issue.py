from bongo.apps.bongo import models
from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = ('id', 'issue_date', 'issue_number', 'volume', 'scribd')
