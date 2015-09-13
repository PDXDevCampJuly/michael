from django.shortcuts import render
from django.http import HttpResponse

def javapic(request):
    return render(request, 'javapic.html')

def join(request):
    return render(request, 'join.html')

def gallery(request):
    return render(request, 'gallery.html')