# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11
from django.conf.urls import url

from . import views
from .views import my_decorator

urlpatterns = [
    # 视图函数的  路由
    # url(r'aclassview/$',views.index),

    #2.类视图  的路由 views.LoginView.as_view == index函数
    url(r'^aclassview/$',views.LoginView.as_view()),
    # url(r'^LoginView_decorator/$',views.LoginView_decorator.as_view()),

    #装饰器路由
    url(r'^LoginView_decorator/$', my_decorator(views.LoginView_decorator.as_view())),

]