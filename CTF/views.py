from django.shortcuts import render
from django.contrib.auth import logout as logout_
from django.contrib.auth.decorators import login_required


# Create your views here.


# TODO: 根据是否已经登录返回 有或者没有 登录注册 按钮的header
def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):
    """
    登出账户
    :param request: 这个我觉得不用说明
    :return: null
    """
    logout_(request)
