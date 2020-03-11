# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^custom_response/$',views.custom_response,name="custom_response"),
    url(r'^response_json/$',views.response_json,name="response_json"),
]