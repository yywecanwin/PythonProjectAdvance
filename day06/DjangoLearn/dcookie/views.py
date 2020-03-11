from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_cookie(request):
    # 1.设置Cookie 1.验证身份 2.保持会话
    response = HttpResponse('操作cookie')
    # HttpResponse.set_cookie(cookie名，value=cookie值，max_age=cookie有效期 秒)
    # response.set_cookie('name','tom',max_age=100)

    # 获取cookie的值
    print(request.COOKIES)
    print(type(request.COOKIES))
    print(request.COOKIES['name'])


    return response
    pass
