# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading

# 任务函数
def task(name,age):
    print("测试")
    task_thread = threading.current_thread()
    print("tack:",task_thread)
    # name,,age
    print("姓名：%s,年龄：%d",name,age)
    pass


if __name__ == '__main__':
    # 获取 当前执行代码的线程
    main_thread = threading.current_thread()
    print("main:",main_thread)
    # 创建子线程
    # sub_thread = threading.Thread(target=task,args=("Tom",18))

    # 启动线程执行任务
    # sub_thread.start()

    # 创建子线程
    sub_thread = threading.Thread(target=task, kwargs={"name":"Tom","age":18})

    # 启动线程执行任务
    sub_thread.start()


    pass


