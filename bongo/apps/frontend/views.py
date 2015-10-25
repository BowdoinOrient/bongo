from django.shortcuts import render
from bongo.apps.bongo import models
from django.http import HttpResponsePermanentRedirect, Http404
from django.core.urlresolvers import reverse
from random import sample, randint


def HomeView(request):

    recent = models.Post.objects.order_by("-published")[:50]

    # @TODO: Pull these from a real model, not this hacked together object
    # also obviously don't do this at random - that's just to catch layout edge cases
    deck = [{
        'post': post,
        'cols': 2,  # randint(1, 4),
        'rows': randint(1, 3),
    } for post in sample(list(recent), randint(4, 7))]

    sections = models.Section.objects.all()

    # extend the sections objects with top posts for each
    for section in sections:
        section.posts = models.Post.objects.filter(section__exact=section.pk).order_by("-published")[:5]

    # section ids:
    # news:         1
    # opinion:      2
    # features:     3
    # artsent:      4
    # sports:       5

    ctx = {
        "news": models.Post.objects.filter(section__exact=1).order_by("-published")[:10],
        "opinion": models.Post.objects.filter(section__exact=2).order_by("-published")[:10],
        "features": models.Post.objects.filter(section__exact=3).order_by("-published")[:10],
        "artsent": models.Post.objects.filter(section__exact=4).order_by("-published")[:10],
        "sports": models.Post.objects.filter(section__exact=5).order_by("-published")[:10],
        "toplist": sorted(recent, key=lambda x: -1 * x.popularity())[:10],
        # this can theoretically raise DoesNotExist but I'm not going to catch: it
        # because if that happens it's a bfd and indicative of some other problem
        "current_issue": models.Issue.objects.order_by("-issue_date").first(),
        "sections": sections,
        # @TODO: pull this from its own model, don't append these attributes here
        "deck": deck
    }

    return render(request, 'pages/home.html', ctx)


def ArticleView(request, id=None, slug=None):
    if id:
        article = models.Post.objects.get(pk__exact=id)
        return HttpResponsePermanentRedirect(reverse(ArticleView, args=[article.slug]))

    ctx = {
        "article": models.Post.objects.get(slug__exact=slug)
    }
    return render(request, 'pages/article.html', ctx)


def AuthorView(request, id=None):
    try:
        creator = models.Creator.objects.get(id__exact=id)
    except models.Creator.DoesNotExist:
        raise Http404("No author with this ID exists")

    ctx = {
        "creator": creator,
        "posts": creator.posts()
    }
    return render(request, 'pages/author.html', ctx)


def SeriesView(request, id=None):
    try:
        series = models.Series.objects.get(id__exact=id)
    except models.Series.DoesNotExist:
        raise Http404("No series with this ID exists")

    ctx = {
        "series": series,
        "posts": series.post_set.all().order_by('-published')
    }

    return render(request, 'pages/series.html', ctx)


def AboutView(request):
    return render(request, 'pages/static/about.html')


def EthicsView(request):
    return render(request, 'pages/static/ethics.html')


def SubscribeView(request):
    return render(request, 'pages/static/subscribe.html')


def AdvertiseView(request):
    return render(request, 'pages/static/advertise.html')


def ContactView(request):
    return render(request, 'pages/static/contact.html')
