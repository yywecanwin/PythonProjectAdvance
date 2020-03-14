from django.contrib import admin

# Register your models here.
from adbs.models import BookInfo,HeroInfo

from django.contrib import admin

admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
