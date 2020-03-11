from django.shortcuts import render
from django.http import HttpResponse

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

