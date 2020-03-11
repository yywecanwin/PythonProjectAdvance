from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse


# Create your views here.
from django.urls import reverse


def custom_response(request):



    # return HttpResponse("操作 响应对象")
    # 1.操作 参数
    # return HttpResponse(
    #     content="浏览器显示的页面",
    #     # 内容类型
    #     content_type='',
    #     # 状态吗
    #     status=202,
    # )

    # 2.操作属性
    response = HttpResponse()
    response.content = "操作属性"
    response.status_code = 200
    return response
    pass

def response_json(request):

    dict_data = {

        'a': 1,
        'b': 3,

    }

    list_data = [
        {
            'a':1,
            'b':3,
        }
    ]
    # 1.默认 只接受dict
    # 2.list_json  需要设置  safe = False 可以传list

    return JsonResponse(list_data,safe=False)
    pass


# 重定向  redicrect
def respose_redicrect(request):

    #重定向 自己的路由
    # return redirect('/auser/index/')
    #反向解析重定向
    print(reverse('auser:index'))
    return redirect(reverse('auser:index'))



    # 重定向别人的网站
    # return redirect("http://www.baidu.com")

    pass

