from .models import MyUser
from time import time
from django.contrib.auth import authenticate, login, logout


def create_user(username, password, email):
    """
    注册普通用户
    :param username: 用户名
    :param password: 密码
    :param email: 邮件
    :return: 成功返回true
    """
    try:
        MyUser.objects.create_user(username=username, password=password, email=email, points=0, admin_level=0,
                                   is_scuer=False, email_verified=False, register_time=time()).save()
        return True
    except:
        return False


def create_superuser(username, password, email):
    """
    注册管理员用户
    :param username: 用户名
    :param password: 密码
    :param email: 邮件
    :return: 成功返回true
    """
    try:
        MyUser.objects.create_user(username=username, password=password, email=email, points=0, is_superuser=True,
                                   admin_level=1, is_scuer=False, email_verified=False, register_time=time()).save()
        return True
    except:
        return False


def try_login(request, username, password):
    user = authenticate(username=username, password=password)
    login(request, user)
