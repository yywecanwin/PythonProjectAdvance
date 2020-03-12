from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


def index(request):

    # 获取请求方法，判断GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return HttpResponse("视图函数---GET--登录页面")

        pass
    else:
        # 处理POST请求 ，实现注册逻辑
        return HttpResponse('视图函数----POST----登录请求')
        pass



    pass


# 定义类视图
class LoginView(View):

    def get(self,request):
        # 处理GET请求，返回注册页面
        return HttpResponse("视图函数---GET--登录页面")
        pass

    def post(self,request):
        # 处理POST请求 ，实现注册逻辑
        return HttpResponse('视图函数----POST----登录请求')

        pass
    pass