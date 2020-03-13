from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class IndexView(View):

    def get(self,request):

        # 渲染模板
        return render(request,'djangoindex.html')

        pass

    def post(self):

        pass

    pass
