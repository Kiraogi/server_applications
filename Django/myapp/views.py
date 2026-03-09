from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render (request, 'myapp/index.html', {'title': 'Главная страница'})

def about(request):
    return render (request, 'myapp/about.html', {'title': 'О нас'})

def products(request):
    items = ["Ноутбук", "Смартфон", "Клавиатура"]
    return render(request, 'myapp/products.html', {'items': items})