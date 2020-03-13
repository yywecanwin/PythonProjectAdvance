# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13


# 1.查询 基本查询  get  all count
from datetime import date

from adbs.models import BookInfo

BookInfo.objects.get(id=2)
BookInfo.objects.all()
BookInfo.objects.count()


# 过滤查询 filter--querySet exclude  get

BookInfo.objects.filter(id=3)
BookInfo.objects.filter(id__exact=3)
BookInfo.objects.exclude(id=3)

# 大于 小于 gt  lt
BookInfo.objects.filter(id__gt=2)

# 包含contains startswith(以什么开头) endswith(以什么结尾)
BookInfo.objects.filter(btitle__contains="天")
BookInfo.objects.filter(btitle__startswith="笑")
BookInfo.objects.filter(btitle__endswith="狐")

# 判断是否为空 is_null
BookInfo.objects.filter(btitle__isnull=True)


#范围 in
BookInfo.objects.filter(id__in=[2,4])

# 日期
BookInfo.objects.filter(bpub_date__year=1995)
BookInfo.objects.filter(bpub_date__gt=date(1995,1,1))


