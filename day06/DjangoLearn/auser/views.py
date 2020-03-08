from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 创建视图函数： 1.接收请求对象 2.解析请求对象 3.model,template 4.返回相应对象
def index(request):

    # 2.返回相应对象 导包快捷键（alt+enter）
    return HttpResponse("hello world 第一次使用Django写项目")
    pass

