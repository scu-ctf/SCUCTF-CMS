from django.db import models


# Create your models here.
class User(models.Model):
    # 用户唯一识别码
    uid = models.IntegerField(blank=False, null=False, unique=True, help_text='用户唯一识别码', primary_key=True)
    # 用户名/昵称
    username = models.CharField(blank=False, null=False, unique=True, max_length=256, help_text='用户名/昵称')
    # 邮箱
    email = models.EmailField(blank=False, null=False, unique=True, max_length=256, help_text='邮箱')
    # 密码
    password = models.CharField(blank=False, null=False, max_length=32, help_text='密码')
    # 积分: 可在商城兑换的积分，不是CTF比赛的积分
    points = models.IntegerField(default=0, blank=False, null=False, help_text='积分')
    # 是否为管理员
    is_admin = models.BooleanField(default=False, blank=False, null=False, help_text='是否为管理员')
    # 管理员等级:
    # 0. 无任何权限
    # 1. 超级管理员
    # 2. 文章管理员
    # 剩下的以后加
    admin_level = models.IntegerField(default=0, blank=False, null=False, help_text='管理员等级')
    # 是否被封
    is_banned = models.BooleanField(default=False, blank=False, null=False, help_text='是否被封')
    # 是否验证邮箱
    is_verify_email = models.BooleanField(default=False, blank=False, null=False, help_text='是否验证邮箱')
    # 是否是本校人员
    is_scuer = models.BooleanField(default=False, blank=False, null=False, help_text='是否是本校人员')
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True, editable=False, help_text='注册时间')
    # 上次登录时间
    last_login = models.DateTimeField(auto_now_add=True, auto_now=True, help_text='上次登录时间')

