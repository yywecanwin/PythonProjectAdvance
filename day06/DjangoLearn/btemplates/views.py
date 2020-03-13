from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


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
            }
        }


        # 渲染模板
        return render(request,'djangoindex.html',context=content)

        pass

    def post(self):

        pass

    pass
