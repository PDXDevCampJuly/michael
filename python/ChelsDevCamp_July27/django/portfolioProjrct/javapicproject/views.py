from django.shortcuts import render

def javapic(request):
    return render(request, 'jsindex.html')

def join(request):
    return render(request, 'join.html')

def gallery(request):
    return render(request, 'gallery.html')