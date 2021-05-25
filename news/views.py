from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def test(request):
    return HttpResponse('it\'s testing page')