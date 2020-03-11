# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11
from django.conf.urls import url
from . import views

urlpatterns = [
    # 末尾加不加 / 看公司要求
    url(r'^custom_response/$',views.custom_response,name="custom_response"),
    # 2.json_response
    url(r'^response_json/$',views.response_json,name="response_json"),
    # 3.重定向：redicrect
    url(r'^respose_redicrect/$',views.respose_redicrect,name="respose_redicrect"),

]