from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {'adjective': "AWESOME"}
    return render(request, 'index.html', content)

def awesome(request):
    return HttpResponse("Corgis are awesome <a href='./'>see ya..</a>")