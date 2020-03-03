from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .auth import try_login, create_user, logout


# Create your views here.


# TODO: 根据是否已经登录返回 有或者没有 登录注册 按钮的header
def index(request):
    return render(request, 'index.html')


def register(request):
    """
    注册账户
    :param request:
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            if create_user(username, password, email):
                return redirect("/CTF/index")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    """
    登录账户
    :param request:
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = try_login(request, username, password)
            if user:
                return redirect("/CTF/index")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    """
    登出账户
    :param request: 这个我觉得不用说明
    :return: null
    """
    logout_(request)
    return redirect("/CTF/index")
