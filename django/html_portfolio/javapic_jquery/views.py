from django.shortcuts import render

def index(request):
    """ main page with image slider """
    return render(request, 'javapic_jquery.html')

def join(request):
    """ join page to access gallery """
    return render(request, 'javapic_jquery_join.html')

def gallery(request):
    """ gallery of images with lightbox effect """
    return render(request, 'javapic_jquery_gallery.html')
