from django.shortcuts import render

def javapic_jquery(request):
    return render(request, 'javapic_jquery.html')

def join(request):
    return render(request, 'javapic_jquery_join.html')

def gallery(request):
    return render(request, 'javapic_jquery_gallery.html')