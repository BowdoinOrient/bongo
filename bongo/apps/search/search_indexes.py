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

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr="title", document=True)
    article_content = indexes.CharField(model_attr="text")
    creators = indexes.CharField(model_attr="creators")
    article_content = indexes.CharField(model_attr="text")
    video_content = indexes.CharField(model_attr="video")
    pdf_content = indexes.CharField(model_attr="pdf")
    photo_content = indexes.CharField(model_attr="photo")
    html_content = indexes.CharField(model_attr="html")
    pullquote_content = indexes.CharField(model_attr="pullquote")
    tags = indexes.CharField(model_attr="tags")

    def get_model(self):
        return Post

    def prepare_article_content(self, obj):
        return [o.body for o in obj.article_set]

    def prepare_video_content(self, obj):
        return [o.caption for o in obj.video_set]

    def prepare_pdf_content(self, obj):
        return [o.caption for o in obj.pdf_set]

    def prepare_photo_content(self, obj):
        return [o.caption for o in obj.photo_set]

    def prepare_html_content(self, obj):
        return [o.caption for o in obj.html_set]

    def prepare_pullquote_content(self, obj):
        return [o.quote for o in obj.pullquote_set] + [o.caption for o in obj.pullquote_set]

    def prepare_tags(self, obj):
        return [o.tag for o in obj.tag_set]
