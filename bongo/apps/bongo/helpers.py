from tagger import tagger
from django.conf import settings
from django.core.cache import cache
import pickle
import os

# Python 3 moves HTMLParser to html.parser
try:
    from HTMLParser import HTMLParser as htmlparse
except ImportError:
    from html.parser import HTMLParser as htmlparse

class MLStripper(htmlparse):
    def __init__(self):
        self.convert_charrefs=False
        self.reset()
        self.fed = []
        self.strict = True
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def tagify(text):
    # cache weights so we don't do this IO repeatedly
    weights = cache.get("weights")
    if not weights:
        with open(os.path.join(settings.SITE_ROOT, "data", "dict.pkl"), 'rb') as f:
            weights = pickle.load(f)
        cache.set("weights", weights, 3600)

    text = strip_tags(text)
    mytagger = tagger.Tagger(
        tagger.Reader(),
        tagger.Stemmer(),
        tagger.Rater(weights)
    )
    return mytagger(text, 5)


def arbitrary_serialize(obj):
    if obj.__class__.__name__ == "Series":
        from bongo.apps.api.serializers.series import SeriesSerializer
        return SeriesSerializer(obj).data
    elif obj.__class__.__name__ == "Volume":
        from bongo.apps.api.serializers.volume import VolumeSerializer
        return VolumeSerializer(obj).data
    elif obj.__class__.__name__ == "Issue":
        from bongo.apps.api.serializers.issue import IssueSerializer
        return IssueSerializer(obj).data
    elif obj.__class__.__name__ == "Section":
        from bongo.apps.api.serializers.section import SectionSerializer
        return SectionSerializer(obj).data
    elif obj.__class__.__name__ == "Tag":
        from bongo.apps.api.serializers.tag import TagSerializer
        return TagSerializer(obj).data
    elif obj.__class__.__name__ == "Job":
        from bongo.apps.api.serializers.job import JobSerializer
        return JobSerializer(obj).data
    elif obj.__class__.__name__ == "Creator":
        from bongo.apps.api.serializers.creator import CreatorSerializer
        return CreatorSerializer(obj).data
    elif obj.__class__.__name__ == "Text":
        from bongo.apps.api.serializers.text import TextSerializer
        return TextSerializer(obj).data
    elif obj.__class__.__name__ == "Video":
        from bongo.apps.api.serializers.video import VideoSerializer
        return VideoSerializer(obj).data
    elif obj.__class__.__name__ == "PDF":
        from bongo.apps.api.serializers.pdf import PDFSerializer
        return PDFSerializer(obj).data
    elif obj.__class__.__name__ == "Photo":
        from bongo.apps.api.serializers.photo import PhotoSerializer
        return PhotoSerializer(obj).data
    elif obj.__class__.__name__ == "Video":
        from bongo.apps.api.serializers.video import VideoSerializer
        return VideoSerializer(obj).data
    elif obj.__class__.__name__ == "HTML":
        from bongo.apps.api.serializers.html import HTMLSerializer
        return HTMLSerializer(obj).data
    elif obj.__class__.__name__ == "Pullquote":
        from bongo.apps.api.serializers.pullquote import PullquoteSerializer
        return PullquoteSerializer(obj).data
    elif obj.__class__.__name__ == "Post":
        from bongo.apps.api.serializers.post import PostSerializer
        return PostSerializer(obj).data
    elif obj.__class__.__name__ == "Alert":
        from bongo.apps.api.serializers.alert import AlertSerializer
        return AlertSerializer(obj).data
    elif obj.__class__.__name__ == "Advertiser":
        from bongo.apps.api.serializers.advertiser import AdvertiserSerializer
        return AdvertiserSerializer(obj).data
    elif obj.__class__.__name__ == "Ad":
        from bongo.apps.api.serializers.ad import AdSerializer
        return AdSerializer(obj).data
    elif obj.__class__.__name__ == "Tip":
        from bongo.apps.api.serializers.tip import TipSerializer
        return TipSerializer(obj).data
    elif obj.__class__.__name__ == "Event":
        from bongo.apps.api.serializers.event import EventSerializer
        return EventSerializer(obj).data
    elif obj.__class__.__name__ == "ScheduledPost":
        from bongo.apps.api.serializers.scheduledpost import ScheduledPostSerializer
        return ScheduledPostSerializer(obj).data
    else:
        raise Exception("Cannot serialize this type: {}".format(obj.__class__.__name____))