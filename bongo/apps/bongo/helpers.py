# from topia.termextract import extract
import tagger
import pickle
import nltk

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
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def tagify(text):
    text = strip_tags(text)

    with open('/tmp/dict.pkl', 'wb') as f:
        tagger.extras.build_dict_from_nltk(f, nltk.corpus.brown,
            nltk.corpus.stopwords.words('english'), measure='ICF')
        weights = pickle.load(f)
        myreader = tagger.Reader()
        mystemmer = tagger.Stemmer()
        myrater = tagger.Rater(weights)
        mytagger = tagger.Tagger(myreader, mystemmer, myrater)
        return mytagger(text, 5)


def arbitrary_serialize(obj):
    from bongo.apps.api import serializers
    if obj.__class__.__name__ == "Series":
        return serializers.SeriesSerializer(obj).data
    elif obj.__class__.__name__ == "Volume":
        return serializers.VolumeSerializer(obj).data
    elif obj.__class__.__name__ == "Issue":
        return serializers.IssueSerializer(obj).data
    elif obj.__class__.__name__ == "Section":
        return serializers.SectionSerializer(obj).data
    elif obj.__class__.__name__ == "Tag":
        return serializers.TagSerializer(obj).data
    elif obj.__class__.__name__ == "Job":
        return serializers.JobSerializer(obj).data
    elif obj.__class__.__name__ == "Creator":
        return serializers.CreatorSerializer(obj).data
    elif obj.__class__.__name__ == "Text":
        return serializers.TextSerializer(obj).data
    elif obj.__class__.__name__ == "Video":
        return serializers.VideoSerializer(obj).data
    elif obj.__class__.__name__ == "PDF":
        return serializers.PDFSerializer(obj).data
    elif obj.__class__.__name__ == "Photo":
        return serializers.PhotoSerializer(obj).data
    elif obj.__class__.__name__ == "Video":
        return serializers.VideoSerializer(obj).data
    elif obj.__class__.__name__ == "HTML":
        return serializers.HTMLSerializer(obj).data
    elif obj.__class__.__name__ == "Pullquote":
        return serializers.PullquoteSerializer(obj).data
    elif obj.__class__.__name__ == "Post":
        return serializers.PostSerializer(obj).data
    elif obj.__class__.__name__ == "Alert":
        return serializers.AlertSerializer(obj).data
    elif obj.__class__.__name__ == "Advertiser":
        return serializers.AdvertiserSerializer(obj).data
    elif obj.__class__.__name__ == "Tip":
        return serializers.TipSerializer(obj).data
    elif obj.__class__.__name__ == "Event":
        return serializers.EventSerializer(obj).data
    elif obj.__class__.__name__ == "ScheduledPost":
        return serializers.ScheduledPostSerializer(obj).data
    else:
        raise Exception("Cannot serialize this type: {}".format(obj.__class__.__name____))