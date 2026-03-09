from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Привет Django!')

def about(request):
    return render (request, 'about.html', {'title': 'О нас'})

