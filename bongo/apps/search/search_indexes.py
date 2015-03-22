from haystack import indexes
from bongo.apps.bongo.models import Creator, Series, Post

class CreatorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='name', document=True)
    user = indexes.CharField(model_attr='user', null=True)
    job = indexes.CharField(model_attr="job", null=True)
    twitter = indexes.CharField(model_attr='twitter', null=True)

    def get_model(self):
        return Creator

class SeriesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='name', document=True)

    def get_model(self):
        return Series