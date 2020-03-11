from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login(request):

    return HttpResponse("1.研究request请求对象 传参  1.1 10/24拼接路劲 1.2 ?a=10&b=20&c=30 1.3 json xml str 1.4 form 1.5 请求头")



    pass

# 解析拼接路径的参数  /1999/beijing
def login_connect(request,city,year):
    print("解析拼接路径的参数----年份：",year)
    print("解析拼接路径的参数----城市：",city)

    return HttpResponse("1.1 10/20/拼接路径参数：")

    pass


# 2.?a=10&b=20&c=30解析查询参数
def brequest_query(request):
    # 解析参数参数 request.GET属性  --->返回类型  django.http.request.QueryDict 支持一健多值
    params = request.GET
    print(params)
    print(type(params))
    print(params.get('b'))
    print(params.getlist('a'))

    return HttpResponse("?a=10&b=20&c=30解析查询参数")

    pass
