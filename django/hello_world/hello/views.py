from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello <a href='/hello/corgi.html'>Corgs?</a>")

def awesome(request):
    return HttpResponse("Corgis are awesome <a href='./'>see ya..</a>")