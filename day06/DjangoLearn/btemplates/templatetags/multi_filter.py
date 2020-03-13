# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

from django import template

# 注册装饰器
register = template.Library()

# 过滤器 函数
@register.filter
def multi(x):
    return x * x

@register.filter
def add(x):
    return x + x

