from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 操作session
def session_response(request):

    # 1.设置session 保存到服务器
    # redis保存的session类型，是字符串

    # 1.1给浏览器 设置了cookies值  sessionid
    # 1.2将name 存储到 redis里面
    # request.session['name'] = 'Tom'
    # request.session['age'] = '66666'

    #2取出session
    # print('取出session值：',request.session['name'])

    # 3.清楚session ，清楚指定key健
    # del request.session['name']

    # 4.清楚seeion 清楚指定的key 健
    # request.session.clear()

    # 5.清楚整条 session
    request.session.flush()

    return HttpResponse("操作 session")

    pass