from django.shortcuts import render
from bongo.apps.bongo import models

def HomeView(request):
    ctx = {}
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