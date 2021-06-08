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


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categoris = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categoris': categoris, 'category': category})
