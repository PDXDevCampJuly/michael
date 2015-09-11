from django.shortcuts import render
from django.http import HttpResponse

def javapic(request):
    return render(request, 'javapic.html')