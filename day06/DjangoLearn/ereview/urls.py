# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/11
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^session_response/$',views.session_response,name="session_response"),

]
