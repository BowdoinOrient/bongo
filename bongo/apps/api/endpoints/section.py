from bongo.apps.bongo.models import Section, Post
from bongo.apps.api.serializers.section import SectionSerializer
from bongo.apps.api.serializers.post import PostSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import list_route
from rest_framework.response import Response


class SectionCrud(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class SectionCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = (filters.OrderingFilter,)

    @list_route()
    def posts(self, request, pk=None):
        if 'limit' in request.GET:
            l = request.GET['limit']
        else:
            l = 10

        if 'ordering' in request.GET:
            s = request.GET["ordering"]
        else:
            s = "-published"

        posts = Post.objects.filter(section_id__exact=pk).order_by(s)[:l]

        serializedPosts = []
        for post in posts:
            serializedPosts.append(PostSerializer(post).data)

        return Response(serializedPosts)
