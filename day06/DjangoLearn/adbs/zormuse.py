# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

# 1.查询 基本查询  get  all count
from datetime import date

from adbs.models import BookInfo

# 增加
book = BookInfo(btitle="西游记",bpub_date=date(1990,1,1))
book.save()

BookInfo.objects.create(btitle="我不",bpub_date=date(2008,12,12))

# 删除
book = BookInfo.objects.get(id=6)
book.delete()

BookInfo.objects.filter(id=5).delete()

# 改
book = BookInfo.objects.get(id=2)
book.btitle = '天龙'
book.save()

BookInfo.objects.filter(id=1).update(bread=20)

# 计算
BookInfo.objects.count()

# 查询 get  all count
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


# 1.两个 字段 对比 过滤 bread__get = bcomment 对象
# 1.查询阅读量大于等于评论量的图书
from django.db.models import F, Sum

BookInfo.objects.filter(bread__gte=F('bcomment'))
# 2.查询评论量大于等于阅读量的二倍
BookInfo.objects.filter(bcomment__gte=F("bread") * 2)

# 2.两个条件  对比  过滤  Q对象  & | ~
from django.db.models import F, Q
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(bread__gt=20,id__lt=3)
BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))

# 例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))

# 查询编号不等于3的图书。exclude()
BookInfo.objects.filter(~Q(id=3))
BookInfo.objects.exclude(id=3)

# 聚合查询 aggregate()
from django.db.models.aggregates import Avg,Sum,Max,Min,Count
BookInfo.objects.aggregate(Sum('id'))
BookInfo.objects.aggregate(Max('bread'))

# 排序 order_by 降序 -
BookInfo.objects.all().order_by("id")
