from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    news = News.objects.all()
    categoris = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categoris': categoris,
    }
    return render(request, 'news/index.html', context)
