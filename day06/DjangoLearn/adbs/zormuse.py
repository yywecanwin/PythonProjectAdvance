# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/13

# 1.查询 基本查询  get  all count
from datetime import date

from adbs.models import BookInfo, HeroInfo

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




# 1.关联查询
# 1:n 1对应的模型类对象 ,多对应的模型类名小写_set
# 根据 书  找书本  对应  所有 英雄
book = BookInfo.objects.get(id=3)
book.heroinfo_set.all()

# n:1
# 英雄  对应的  书

hero = HeroInfo.objects.get(id=11)
hero.hbook

hero.hbook_id  # 1

# 2.关联过滤查询  关联模型类型名小写__属性名___条件运算符=值
# 多模型类条件查询-模型类数据: n:1
# 查询图书 ,要求图书英雄为"东方不败"

BookInfo.objects.filter(heroinfo__hname__exact="东方不败")

# 由一模型类条件查询多模型类数据:一模型类关联属性名__一模型类属性名__条件运算符=值
# 查询书名为“天龙八部”的所有英雄。
HeroInfo.objects.filter(hbook__btitle__exact="天龙")

#查询图书阅读量大于30的所有英雄
HeroInfo.objects.filter(hbook__btitle__gt=30)


# querySet类型

# 1.惰性加载  懒加载
qs = BookInfo.objects.filter(id__lt=3)
qs

# 2.缓存
[q for q in qs]
[q for q in qs]

# objects --自定义 管理器 对象 Manager

# 1.系统方法  改
# 2.新增自己的方法



