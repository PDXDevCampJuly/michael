from django.shortcuts import render
# from django.http import HttpResponse

def zen_mockup(request):
    return render(request, 'zen_mockup.html')
