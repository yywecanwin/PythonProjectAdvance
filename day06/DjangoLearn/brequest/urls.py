# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.login,name='login'),
    #1.2008/beijing/拼接路径参数 直接正则匹配
    # url(r'^login_connect/(\d{4})/([a-z]+)/$',views.login_connect),
    #1.2008/beijing/拼接路径参数 直接正则匹配 给 正则起名字 获取的时候就可以不根据顺序
    url(r'^login_connect/(?P<year>\d{4})/(?P<city>[a-z]+)/$', views.login_connect),

    url(r'brequest_query/$',views.brequest_query),

    url(r'^login_form/$',views.login_form,name="login_form"),

]