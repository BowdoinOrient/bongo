from bongo.apps.bongo import models
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Series
        fields = ('id', 'name',)

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Volume
        fields = ('id', 'volume_number', 'volume_year_start', 'volume_year_end')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = ('id', 'issue_date', 'issue_number', 'volume', 'scribd')

class SectionSerializer(serializers.ModelSerializer):
    classname = serializers.ReadOnlyField()

    class Meta:
        model = models.Section
        fields = ('id', 'section', 'classname', 'priority')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'tag',)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'title',)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Creator
        fields = ('id', 'user', 'name', 'job', 'twitter', 'profpic', 'courtesyof')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = ('id', 'creators', 'caption', 'body', 'excerpt')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('id', 'creators', 'caption', 'host', 'uid')

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PDF
        fields = ('id', 'creators', 'caption', 'staticfile')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ('id', 'creators', 'caption', 'staticfile')

class HTMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HTML
        fields = ('id', 'creators', 'caption', 'content')

class PullquoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pullquote
        fields = ('id', 'creators', 'caption', 'quote', 'attribution')

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

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alert
        fields = ('id', 'run_from', 'run_through', 'message', 'urgent')

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advertiser
        fields = ('id', 'name',)

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ad
        fields = ('id', 'run_from', 'run_through', 'owner', 'url', 'adfile')

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tip
        fields = ('id', 'content', 'respond_to', 'submitted_at', 'submitted_from', 'useragent')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id', )

class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScheduledPost
        fields = ('id', )
