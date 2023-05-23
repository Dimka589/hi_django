from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 12 +1
    return render(request, 'about.html', {'asd': a})

def home(request):
    return HttpResponse('this is not my home')