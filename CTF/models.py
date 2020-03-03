from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 用户唯一识别码
    uid = models.IntegerField(blank=False, null=False, unique=True, help_text='用户唯一识别码', primary_key=True)

    # 用户名/昵称（已经被系统实现了）
    # username = models.CharField(blank=False, null=False, unique=True, max_length=256, help_text='用户名/昵称')
    # 邮箱（已经被系统实现了）
    # email = models.EmailField(blank=False, null=False, unique=True, max_length=256, help_text='邮箱')
    # 密码（已经被系统实现了，哈希保存）
    # password = models.CharField(blank=False, null=False, max_length=32, help_text='密码')

    # 头像路径
    avatar = models.CharField(default="/static/upload/avatar.jpg", blank=False, null=True, unique=True, max_length=64,
                              help_text='头像')

    # 积分: 可在商城兑换的积分，不是CTF比赛的积分
    points = models.IntegerField(default=0, blank=False, null=False, help_text='积分')
    # 是否为管理员（已经被系统实现了，名为is_superuser）
    # is_admin = models.BooleanField(default=False, blank=False, null=False, help_text='是否为管理员')

    # 管理员等级:
    # 0. 无任何权限
    # 1. 超级管理员
    # 2. 文章管理员
    # 剩下的以后加
    admin_level = models.IntegerField(default=0, blank=False, null=False, help_text='管理员等级')

    # 是否被封（已经被系统实现了，名为is_active）
    # is_banned = models.BooleanField(default=False, blank=False, null=False, help_text='是否被封')

    # 是否是本校人员
    is_scuer = models.BooleanField(default=False, blank=False, null=False, help_text='是否是本校人员')
    # 邮箱是否经过验证
    email_verified = models.BooleanField(default=False, blank=False, null=False, help_text='邮箱是否经过验证')
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True, editable=False, help_text='注册时间')

    # 上次登录时间（已经被系统实现了）
    # last_login = models.DateTimeField(auto_now_add=True, auto_now=True, help_text='上次登录时间')
    class Meta(AbstractUser.Meta):
        pass
