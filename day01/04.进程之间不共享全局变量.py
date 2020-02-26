# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import multiprocessing
import time

# # 测试代码
# reult = type([])
# print(type(reult)) #<class 'type'>

# dinginess全局变量
g_list = list()  # => 表示一个空列表


# 向全局变量添加数据
def add_data():
    for i in range(3):
        g_list.append(i)
        print("add_data:", i)
        time.sleep(0.2)
        pass
    print("数据添加完毕：", g_list)
    pass


# 读取全局变量数据
def read_data():
    print("read_data:", g_list)
    pass


if __name__ == '__main__':
    # 添加数据进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 读取数据进程
    read_data_process = multiprocessing.Process(target=read_data)

    # 启动进程执行对应的任务
    add_data_process.start()
    # 进程等待join,主进程会等待子进程（add_data_process）执行完成以后，在继续执行下面的代码
    add_data_process.join()
    read_data_process.start()

    print("获取主进程里面的", g_list)
    pass
