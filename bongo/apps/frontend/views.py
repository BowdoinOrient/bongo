from django.shortcuts import render
from bongo.apps.bongo import models

def HomeView(request):

    recent = models.Post.objects.order_by("-published")[:50]

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
        # this can theoretically raise DoesNotExist but I'm not going to catch: it because if that happens it's a bfd and indicative of some other problem
        "current_issue": models.Issue.objects.order_by("-issue_date").first(),
        "sections": sections
    }

    return render(request, 'pages/home.html', ctx)

def ArticleView(request):
    ctx = {}
    return render(request, 'pages/article.html', ctx)

def AuthorView(request):
    ctx = {}
    return render(request, 'pages/author.html', ctx)

def SeriesView(request):
    ctx = {}
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