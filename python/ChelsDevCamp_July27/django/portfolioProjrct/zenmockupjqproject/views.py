from django.shortcuts import render

def zen(request):
    return render(request, 'zen_mockup.html')