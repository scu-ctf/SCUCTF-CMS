from django.urls import path
from . import views

app_name = "CTF"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('index/', views.index, name="index"),
]