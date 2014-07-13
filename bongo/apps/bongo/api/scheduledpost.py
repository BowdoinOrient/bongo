from bongo.apps.bongo.models import ScheduledPost
from bongo.apps.bongo.serializers import ScheduledPostSerializer
from rest_framework import generics

class ScheduledPostList(generics.ListCreateAPIView):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer

class ScheduledPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer