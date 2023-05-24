from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 12 +1
    return render(request, 'about.html', {'asd': a})

def home(request):
    return render(request, 'home.html')

def reverse(request):
    return render(request, 'homereverse.html')