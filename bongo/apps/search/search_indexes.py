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
    article_content = indexes.MultiValueField()
    creators = indexes.MultiValueField()
    article_content = indexes.MultiValueField()
    video_content = indexes.MultiValueField()
    pdf_content = indexes.MultiValueField()
    photo_content = indexes.MultiValueField()
    html_content = indexes.MultiValueField()
    pullquote_content = indexes.MultiValueField()
    tags = indexes.MultiValueField()
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Post

    def prepare_article_content(self, obj):
        return [o.body for o in obj.text.all()]

    def prepare_video_content(self, obj):
        return [o.caption for o in obj.video.all()]

    def prepare_pdf_content(self, obj):
        return [o.caption for o in obj.pdf.all()]

    def prepare_photo_content(self, obj):
        return [o.caption for o in obj.photo.all()]

    def prepare_html_content(self, obj):
        return [o.caption for o in obj.html.all()]

    def prepare_pullquote_content(self, obj):
        return [o.quote for o in obj.pullquote.all()] + [o.caption for o in obj.pullquote.all()]

    def prepare_tags(self, obj):
        return [o.tag for o in obj.tags.all()]
