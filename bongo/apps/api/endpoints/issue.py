from bongo.apps.bongo.models import Issue
from bongo.apps.api.serializers.issue import IssueSerializer
from rest_framework import viewsets, permissions, filters


class IssueCrud(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class IssueCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = (filters.OrderingFilter,)
