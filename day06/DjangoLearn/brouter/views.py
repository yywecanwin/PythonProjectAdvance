from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):

    return HttpResponse('研究功能 路由屏蔽')
    pass

def login_one(request):

    return HttpResponse("222222222222")
    pass

