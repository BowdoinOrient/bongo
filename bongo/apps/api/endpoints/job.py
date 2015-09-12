from bongo.apps.bongo.models import Job
from bongo.apps.api.serializers.job import JobSerializer
from rest_framework import viewsets, permissions, filters


class JobCrud(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class JobCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (filters.OrderingFilter,)
