"""DjangoLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/',admin.site.urls),

#     总路由找子路由
    url(r'^auser/',include('auser.urls',namespace='auser')),
    #brouter 路由
    # url(r'brouter/',include('brouter.urls',namespace='brouter')),
    url(r'brouter/',include('brouter.urls')),
    #定义request的应用
    url(r'^brequest/',include('brequest.urls',namespace='brequest')),
    #定义cresponse的应用
    url(r'^cresponse/',include('cresponse.urls',namespace='cresponse')),
    # 定义cookie应用
    url(r'^dcookie/',include('dcookie.urls',namespace='dcookie')),
    #定义session应用
    url(r'^ereview/',include('ereview.urls',namespace="ereview")),

    #定义类似图
    url(r'^aclassview/',include('aclassview.urls',namespace='aclassview')),

    #定义模板渲染路由
    url(r'^btemplates/',include('btemplates.urls',namespace='btemplate')),

    url(r'^adbs/',include('adbs.urls',namespace='abds')),


]
