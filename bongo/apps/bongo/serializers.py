from bongo.apps.bongo.models import *
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name',)

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('id', 'volume_number', 'volume_year_start', 'volume_year_end')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'issue_date', 'issue_number', 'volume', 'scribd')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'section', 'priority')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag',)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title',)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('id', 'user', 'name', 'job', 'twitter', 'profpic', 'courtesyof')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'creators', 'caption')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'creators', 'caption', 'body', 'excerpt')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'creators', 'caption', 'host', 'uid')

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ('id', 'creators', 'caption', 'staticfile')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'creators', 'caption', 'staticfile')

class HTMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTML
        fields = ('id', 'creators', 'caption', 'content')

class PullquoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pullquote
        fields = ('id', 'creators', 'caption', 'quote', 'attribution')

class PostSerializer(serializers.ModelSerializer):
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
            'creators',
            'content',
            'primary_type'
        )

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'run_from', 'run_through', 'message', 'urgent')

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ('id', 'name',)

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'run_from', 'run_through', 'owner', 'url', 'adfile')

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'content', 'respond_to', 'submitted_at', 'submitted_from', 'useragent')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', )

class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPost
        fields = ('id', )
