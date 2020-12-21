from django import forms   
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken")
        return email
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username",]

class ProfileUpdateForm(forms.ModelForm):   
    class Meta:
        model = Profile
        fields = ['image']