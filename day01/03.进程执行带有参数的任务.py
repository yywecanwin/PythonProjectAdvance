# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/25

import multiprocessing


def task(count, name):
    # print(count)
    print(name)
    print(multiprocessing.current_process())
    for i in range(3):
        print("%d任务执行中。。。" % i)
        pass

    pass


if __name__ == '__main__':
    # 创建子进程
    # 元组如果只有一个元素，那么元素后面的逗号不能省略
    # args:表示以元组方式给执行任务传参数，实际上是按照函数位置参数进行传参的
    # sub_process = multiprocessing.Process(target=task,args=(2,"张三"),name="sub_process")
    # sub_process.start()

    # kwargs：表示以字典方式执行任务传参数，实际上是按照函数关键字（key值）传参的
    sub_process = multiprocessing.Process(target=task, kwargs={"name": "tom", "count": 1})
    sub_process.start()

    pass
