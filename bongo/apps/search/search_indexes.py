from haystack import indexes
from bongo.apps.bongo.models import Creator, Series, Post

class CreatorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='name', document=True, use_template=True)

    def get_model(self):
        return Creator

class SeriesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='name', document=True, use_template=True)

    def get_model(self):
        return Series

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr="title", document=True, use_template=True)
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Post

    def get_updated_field(self):
        return "updated"