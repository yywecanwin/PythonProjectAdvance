from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
import json


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

# 3.请求体--form表单参数的  解析
def login_form(request):
    params = request.POST
    print(params)
    print(type(params))
    # print(params.getlist('a'))
    # print(params.get('a'))

    return HttpResponse("3.form表单参数的  解析")

    pass

# 非form表单参数的解析
# json xml  str
def login_not_form(request):
    # 解析 非form表单的参数，request.boby  返回的对象是  二进制  bytes
    b_data = request.body
    # print(b_data)
    # print(type(b_data))
    # print(b_data.decode()) #二进制转字符串

    # 如果 参数 是 json的   bytes-->str--->dict
    # 如果参数json参数，先将二进制转换成字符串，再将字符串转换成字典
    str_one = b_data.decode()
    dict_data = json.loads(str_one)
    print(dict_data)
    print(type(dict_data))

    return HttpResponse('json xml  str')

    pass
