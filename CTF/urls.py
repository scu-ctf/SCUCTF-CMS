from django.urls import path
from . import views
from django.conf.urls import url

app_name = "CTF"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name="index"),

]