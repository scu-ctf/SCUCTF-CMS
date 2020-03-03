from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout as logout_
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .auth import create_user, try_login
from SCUCTF_CMS.settings import STATIC_URL
from .utils import util


# Create your views here.


def index(request):
    """
    首页显示，如果已经登录，就显示个人中心，不显示登录和注册按钮
    如果未登录，就显示登录和注册按钮，不显示个人中心
    :param request: 用户请求
    :return: 返回渲染后页面
    """
    if request.user.is_authenticated:
        return render(request, 'index.html', {
            'user': request.user
        })
    else:
        return render(request, 'index.html')


def register(request):
    """
    注册账户
    :param request:
    """
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            if create_user(username, password, email):
                return redirect(index)
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    """
    登录账户
    :param request:
    """
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if try_login(request, username, password):
                next_url = request.GET.get('next', False)
                if next_url:
                    return HttpResponseRedirect(next_url)
                return redirect(index)
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


@login_required
def user_center(request):
    """
    个人中心页面，根据setting_type判断用户更改了哪些资料，若没有setting_type或设置错误，则返回用户信息
    :param request:
    :return:
    """
    if request.method == 'POST':
        setting_type = request.POST.get('type', None)
        if not setting_type:
            return render('user_center.html', request, {
                'user': request.user
            })
        # 设置头像
        if setting_type == 1:
            avatar = request.FILES.get("avatar", None)
            # 没有对头像文件格式进行检查直接按照jpg存放
            if avatar:
                path = STATIC_URL + util.random_md5()
                f = open('%s.png' % path, 'wb+')
                for chunk in avatar.chunks():
                    f.write(chunk)
                f.close()
                request.user.save(avatar=path)
                return render(request, 'user_center.html', {
                    'user': request.user,
                    'tips': '头像修改成功'
                })
            return render(request, 'user_center.html', {
                'user': request.user,
                'tips': '请上传头像'
            })
        # 保留
        elif setting_type == 2:
            pass
        # 更改密码
        elif setting_type == 3:
            pass
        # 川大认证
        elif setting_type == 4:
            pass
        else:
            return render('user_center.html', request, {
                'user': request.user,
                'tips': '参数错误'
            })
    print(request.user.username)
    return render(request, 'user_center.html', {
        'user': request.user
    })
