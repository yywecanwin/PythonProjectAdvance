# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/10
from django.conf.urls import url
from . import views

urlpatterns = [
    #不规范的写法因为路由的执行的顺序  从下到上  所以屏蔽
    # url(r'login',views.login),
    # url(r'login_one',views.login_one),

    url(r'^login$',views.login,name="login"),
    url(r'^login_one$',views.login_one,name="register"),
]