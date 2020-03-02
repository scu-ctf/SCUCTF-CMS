from django.shortcuts import render

# Create your views here.


# TODO: 根据是否已经登录返回 有或者没有 登录注册 按钮的header
def index(request):
    return render(request, 'index.html')

