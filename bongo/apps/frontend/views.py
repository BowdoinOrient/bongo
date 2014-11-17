from django.shortcuts import render
from bongo.apps.bongo import models
from random import choice

def HomeView(request):

    recent = models.Post.objects.order_by("-published")[:100]

    sections = models.Section.objects.all()

    section_ids = {
        "news": 1,
        "opinion": 2,
        "features": 3,
        "artsent": 4,
        "sports": 5
    }

    ctx = {
        "news": choice(models.Post.objects.filter(section__exact=section_ids['news'])),
        "features": choice(models.Post.objects.filter(section__exact=section_ids['features'])),
        "artsent": choice(models.Post.objects.filter(section__exact=section_ids['artsent'])),
        "sports": choice(models.Post.objects.filter(section__exact=section_ids['sports'])),
        "op1": choice(models.Post.objects.filter(section__exact=section_ids['opinion'])),
        "op2": choice(models.Post.objects.filter(section__exact=section_ids['opinion'])),
        "toplist": sorted(recent, key=lambda x: -1 * x.popularity())[:10],
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