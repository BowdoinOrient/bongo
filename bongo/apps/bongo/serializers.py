from django.db import models
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('name',)

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('volume_number', 'volume_year_start', 'volume_year_end')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('issue_date', 'issue_number', 'volume', 'scribd')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('section', 'priority')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title',)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('user', 'name', 'job', 'twitter', 'profpic', 'courtesyof')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('creators', 'caption')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('creators', 'caption', 'body', 'excerpt')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('creators', 'caption', 'host', 'uid')

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ('creators', 'caption', 'staticfile')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('creators', 'caption', 'staticfile')

class HTMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTML
        fields = ('creators', 'caption', 'content')

class PullquoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pullquote
        fields = ('creators', 'caption', 'quote', 'attribution')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
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
        fields = ('run_from', 'run_through', 'message', 'urgent')

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ('name',)

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('run_from', 'run_through', 'owner', 'url', 'adfile')

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('content', 'respond_to', 'submitted_at', 'submitted_from', 'useragent')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ()

class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPost
        fields = ()
