from django import forms
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

