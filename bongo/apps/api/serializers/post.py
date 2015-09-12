from bongo.apps.bongo import models
from rest_framework import serializers
from ..serializers.text import TextSerializer
from ..serializers.video import VideoSerializer
from ..serializers.pdf import PDFSerializer
from ..serializers.photo import PhotoSerializer
from ..serializers.html import HTMLSerializer
from ..serializers.pullquote import PullquoteSerializer


class PostSerializer(serializers.ModelSerializer):
    content = serializers.ReadOnlyField()
    creators = serializers.ReadOnlyField()

    class Meta:
        model = models.Post
        fields = (
            'id',
            'created',
            'updated',
            'published',
            'is_published',
            'series',
            'issue',
            'volume',
            'section',
            'title',
            'slug',
            'tags',
            'opinion',
            'views_local',
            'views_global',
            'content',
            'creators',
            'primary_type'
        )

    def get_content(self, obj):
        return {
            "text": TextSerializer(self.text.all(), many=True),
            "video": VideoSerializer(self.video.all(), many=True),
            "pdf": PDFSerializer(self.pdf.all(), many=True),
            "photo": PhotoSerializer(self.photo.all(), many=True),
            "html": HTMLSerializer(self.html.all(), many=True),
            "pullquote": PullquoteSerializer(self.pullquote.all(), many=True)
        }
