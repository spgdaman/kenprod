from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = User
        fields = ('username', 'first_name', 'last_name',)