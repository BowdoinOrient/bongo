import factory
from bongo.apps.bongo import models
from random import choice, sample
from string import lowercase, digits

class ContentFactory(factory.Factory):
    class Meta:
        model = models.Content

    caption = factory.Sequence(lambda n: 'This is content #{0}'.format(n))

class TextFactory(factory.Factory):
    class Meta:
        model = models.Text

    caption = factory.Sequence(lambda n: 'This is text #{0}'.format(n))
    body = "It has a loooooooooooooong body"
    excerpt = "The excerpt isn't correct until it's saved"

class VideoFactory(factory.Factory):
    class Meta:
        model = models.Video

    caption = factory.Sequence(lambda n: 'This is video #{0}'.format(n))
    host = choice(["Vimeo", "YouTube", "Vine"])
    uid = ''.join(choice(lowercase + digits) for i in range(15))

class PDFFactory(factory.Factory):
    class Meta:
        model = models.PDF

    caption = factory.Sequence(lambda n: 'This is pdf #{0}'.format(n))

class PhotoFactory(factory.Factory):
    class Meta:
        model = models.Photo

    caption = factory.Sequence(lambda n: 'This is photo #{0}'.format(n))

class HTMLFactory(factory.Factory):
    class Meta:
        model = models.HTML

    caption = factory.Sequence(lambda n: 'This is html #{0}'.format(n))
    content = "<h1>wooo html</h1>"

class PullquoteFactory(factory.Factory):
    class Meta:
        model = models.Pullquote

    caption = factory.Sequence(lambda n: 'This is pullquote #{0}'.format(n))
    quote = "Success is my only motherfuckin' option, failure's not"
    attribution = "Marshall Mathers, TDD evangelist"