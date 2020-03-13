# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

# 定义自己的中间件
def simple_middleware(get_response):

    # 初始化 init
    print("中间件111----init----DEBUG模式  执行2次")

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图欠被调用
        print("中间件1111-----处理请求对象之前----")

        response = get_response(request)


        # 此处编写的代码会在每个请求处理视图之后被调用

        print("中间件1111-----处理请求对象之后------")
        return response


        pass
    return middleware

    pass




