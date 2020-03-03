from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .auth import try_login, create_user, logout


# Create your views here.


def index(request):
    """
    首页显示，如果已经登录，就显示个人中心，不显示登录和注册按钮
    如果未登录，就显示登录和注册按钮，不显示个人中心
    :param request: 用户请求
    :return: 返回渲染后页面
    """
    if request.user.is_authenticated():
        return render(request, 'index.html',  {
            'user': request.user
        })
    return render(request, 'index.html')


def register(request):
    """
    注册账户
    :param request:
    """
    if request.method == 'POST' and not request.user.is_active:
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
    if request.method == 'POST' and not request.user.is_authenticated:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = try_login(request, username, password)
            if user.is_authenticated:
                return redirect(index)
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
    if request.user.is_authenticated:
        logout_(request)
        return redirect(index)
    return redirect(index)
