from django.shortcuts import render

def javapic(request):
    """ main page with image slider """
    return render(request, 'javapic.html')

def join(request):
    """ join page to access gallery """
    return render(request, 'javapic_join.html')

def gallery(request):
    """ gallery of images with lightbox effect """
    return render(request, 'javapic_gallery.html')
