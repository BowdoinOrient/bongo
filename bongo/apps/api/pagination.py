from __future__ import unicode_literals

from rest_framework import pagination
from rest_framework import serializers


class BongoPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'limit'
    max_page_size = 100
