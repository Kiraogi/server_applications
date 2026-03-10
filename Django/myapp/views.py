from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import NameForm, UserProfileForm


def home(request):
    return render (request, 'myapp/index.html', {'title': 'Главная страница'})

def about(request):
    return render (request, 'myapp/about.html', {'title': 'О нас'})

def products(request):
    items = ["Ноутбук", "Смартфон", "Клавиатура"]
    return render(request, 'myapp/products.html', {'items': items})

def submit_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            messages.success(request, "Форма успешна отправлена.")
            name = form.cleaned_data["name"]
            return render(request, "success.html", {'name': name})
        else:
            messages.error(request, "Ошибка, Проверьте данные.")
            form = NameForm()
        return render(request, "form.html", {"form": form})
    
def register(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save() # Сохранить в базу данных
            return redirect("success")
        else:
            form = UserProfileForm
        return render(request, "register.html", {"form": form})
