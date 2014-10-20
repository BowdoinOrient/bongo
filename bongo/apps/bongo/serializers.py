from bongo.apps.bongo.models import *
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name',)
        depth = 2

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('id', 'volume_number', 'volume_year_start', 'volume_year_end')
        depth = 2

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'issue_date', 'issue_number', 'volume', 'scribd')
        depth = 2

class SectionSerializer(serializers.ModelSerializer):
    classname = serializers.Field(source='classname')

    class Meta:
        model = Section
        fields = ('id', 'section', 'classname', 'priority')
        depth = 2

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag',)
        depth = 2

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title',)
        depth = 2

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('id', 'user', 'name', 'job', 'twitter', 'profpic', 'courtesyof')
        depth = 2

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'creators', 'caption', 'body', 'excerpt')
        depth = 2

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'creators', 'caption', 'host', 'uid')
        depth = 2

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ('id', 'creators', 'caption', 'staticfile')
        depth = 2

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'creators', 'caption', 'staticfile')
        depth = 2

class HTMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTML
        fields = ('id', 'creators', 'caption', 'content')
        depth = 2

class PullquoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pullquote
        fields = ('id', 'creators', 'caption', 'quote', 'attribution')
        depth = 2

class PostSerializer(serializers.ModelSerializer):
    content = serializers.Field(source='content')
    creators = serializers.Field(source='creators')
    section = SectionSerializer()

    class Meta:
        model = Post
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
        depth = 2

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'run_from', 'run_through', 'message', 'urgent')
        depth = 2

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ('id', 'name',)
        depth = 2

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'run_from', 'run_through', 'owner', 'url', 'adfile')
        depth = 2

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'content', 'respond_to', 'submitted_at', 'submitted_from', 'useragent')
        depth = 2

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', )
        depth = 2

class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPost
        fields = ('id', )
