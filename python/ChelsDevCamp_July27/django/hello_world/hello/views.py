from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    Content = {'someadjective': "CUTE",
               'adjtwo': 'Amazing'}
    return render(request, 'index.html', Content)

def corgi(request):
    return HttpResponse("Corgis are awesome! <a href='/hello'>Go to homepage</a>")

def forum(request):
    return render(request, 'ForumHtml.html')