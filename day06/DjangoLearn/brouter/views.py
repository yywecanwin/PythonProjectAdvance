from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse


def login(request):
    # 路由反解析 --根据  视图函数  request 反向推理当前  路由是什么？reverse()

    # 1.有namespace name反向解析 ----：resverse("")
    print("有namespace反向解析 ----：",reverse('brouter:login'))


    return HttpResponse('研究功能 路由屏蔽')
    pass

def login_one(request):
    # 2.没有namespace name反向解析 ----：resverse("")
    print("有namespace反向解析 ----：", reverse('register'))

    return HttpResponse("222222222222")
    pass

