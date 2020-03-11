from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

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

