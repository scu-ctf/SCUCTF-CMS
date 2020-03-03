from django.urls import path, re_path
from . import views
from django.conf.urls import url

app_name = "CTF"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name="index"),
    path('user_center/', views.user_center, name='user_center')
]
