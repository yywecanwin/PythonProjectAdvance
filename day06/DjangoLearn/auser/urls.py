# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/8

# 子应用 自己管理自己的路由

from django.conf.urls import url
from auser import views

urlpatterns = [
    #子路由
    url(r'^index',views.index,name='index'),
]
