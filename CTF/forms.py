from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=150)
    password = forms.CharField(label="密码", max_length=32, widget=forms.PasswordInput)
