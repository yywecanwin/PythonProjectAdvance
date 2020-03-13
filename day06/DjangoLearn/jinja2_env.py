# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.filters['sum'] = sum

    return env

# 1.定义过滤器
def sum(x):
    return x + x
    pass
