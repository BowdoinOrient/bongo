from __future__ import unicode_literals

from rest_framework import pagination
from rest_framework import serializers

class LinksSerializer(serializers.Serializer):
    next = pagination.NextPageField(source='*')
    prev = pagination.PreviousPageField(source='*')

class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    links = LinksSerializer(source='*')  # Takes the page object as the source
    total_results = serializers.ReadOnlyField(source='paginator.count')

    results_field = 'objects'