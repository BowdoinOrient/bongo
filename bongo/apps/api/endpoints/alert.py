from bongo.apps.bongo.models import Alert
from bongo.apps.api.serializers.alert import AlertSerializer
from rest_framework import viewsets, permissions, filters

class AlertCrud(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class AlertCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = (filters.OrderingFilter,)