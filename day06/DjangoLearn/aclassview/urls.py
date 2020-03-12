# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11
from django.conf.urls import url

from . import views

urlpatterns = [
    # 视图函数的  路由
    # url(r'aclassview/$',views.index),

    #2.类视图  的路由 views.LoginView.as_view == index函数
    url(r'^aclassview/$',views.LoginView.as_view()),

]