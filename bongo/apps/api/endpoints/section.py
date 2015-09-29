from bongo.apps.bongo.models import Section, Post
from bongo.apps.api.serializers.section import SectionSerializer
from bongo.apps.api.serializers.post import PostSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.conf import settings


class SectionCrud(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class SectionCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = (filters.OrderingFilter,)

    @detail_route()
    def posts(self, request, version=settings.REST_FRAMEWORK['DEFAULT_VERSION'], pk=None):
        if 'limit' in request.GET:
            l = int(request.GET['limit'])
        else:
            l = 10

        if 'ordering' in request.GET:
            s = request.GET["ordering"]
        else:
            s = "-published"

        posts = Section.objects.get(pk__exact=pk).post_set.all().order_by(s)[:l]

        serializedPosts = []
        for post in posts:
            serializedPosts.append(PostSerializer(post).data)

        serializedPosts = {"posts": serializedPosts}

        return Response(serializedPosts)
