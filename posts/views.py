from django.shortcuts import render
from django.core import serializers
from . models import feed
import json
# Create your views here.


def index(request):
    template = 'posts/index.html'
    results = feed.objects.all()
    context = {
        'results': results,
    }
    return render(request, template, context)


def base_layout(request):
    template = 'posts/base.html'
    return render(request, template)
