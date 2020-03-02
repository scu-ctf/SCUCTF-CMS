from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)