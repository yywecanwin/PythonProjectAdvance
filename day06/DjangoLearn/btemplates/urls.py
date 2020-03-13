# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^btemplate_index/',views.IndexView.as_view()),
]