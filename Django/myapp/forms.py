from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class NameForm(forms.Form):
    name = forms.CharField(label="Введите имя",min_length=3, max_length=100)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if "@" in name:
            raise forms.ValidationError("Имя не должно содержать - @")
        return name
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "email"]

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            raise forms.ValidationError("Пароль не совпадает")
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
