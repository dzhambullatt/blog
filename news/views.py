from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.order_by('-created_ad')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)
