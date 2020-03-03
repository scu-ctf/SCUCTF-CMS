from django.urls import path
from . import views

app_name = "CTF"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name="index"),
]