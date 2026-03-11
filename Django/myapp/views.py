from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .forms import NameForm, UserProfileForm, RegisterForm, LoginForm
from .api.serializers import UserProfileSerializer


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


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserList(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"]) # Шифруем пароль
            user.save()
            login(request, user) # Автоматический вход после регистрации
            return redirect("home")
        else:
            form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Неверный учетные данные")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})    