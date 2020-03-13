from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
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


# 1.装饰器 装饰器函数的
def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print("添加了装饰器---函数")
        print(request.method,request.path)
        return func(request,*args,**kwargs)
        pass

    return wrapper


# 1.装饰器 装饰器函数的
def my_decorator_self(func):
    def wrapper(self,request,*args,**kwargs):
        print("添加了装饰器---函数")
        print(request.method,request.path)
        return func(self,request,*args,**kwargs)
        pass

    return wrapper



# 给类视图  添加装饰器
@method_decorator(my_decorator,name='dispatch')
class LoginView_decorator(View):
    # @my_decorator_self
    def get(self,request):
        # 处理GET请求，返回注册页面
        return HttpResponse("视图函数--装饰器-GET--登录页面")
        pass

    def post(self,request):
        # 处理POST请求 ，实现注册逻辑
        return HttpResponse('视图函数--装饰器--POST----登录请求')

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