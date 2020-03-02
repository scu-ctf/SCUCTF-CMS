from django.shortcuts import render
from django.contrib.auth import logout as logout_
from django.contrib.auth.decorators import login_required


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


@login_required
def logout(request):
    """
    登出账户
    :param request: 这个我觉得不用说明
    :return: null
    """
    logout_(request)
