from bongo.apps.bongo.models import Post
from bongo.apps.api.serializers.post import PostSerializer
from rest_framework import viewsets, permissions, filters


class PostCrud(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class PostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter,)
