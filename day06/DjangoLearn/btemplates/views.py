from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from datetime import date


class IndexView(View):

    def get(self,request):
        content = {
            "name":'老王',
            "age":88,
            "son":[
                "小明",
                "小王",
                "大头儿子"
            ],
            "wife":{
                "name":"小丽",
            },
            "date_time":date(2018,1,1),
            "data":"<a href='http://www.baidu.com'>百度</a>",
        }


        # 渲染模板
        return render(request,'djangoindex.html',context=content)

        pass

    def post(self):

        pass

    pass
