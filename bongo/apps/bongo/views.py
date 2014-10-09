from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def custom404(request):
    return render(request, "custom404.html", status=404)