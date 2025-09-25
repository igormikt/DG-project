from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Project Start</h1>")

def data(request):
    return HttpResponse("<h1>Это страница data Project Start</h1>")

def test(request):
    return HttpResponse("<h1>Это еще одна страница test Project Start</h1>")

# Create your views here.
