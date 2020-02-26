# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading
import time

# 定义全局变量列表

q_list = []


# 向全局变量里面添加数据
def add_data():
    for i in range(10):
        q_list.append(i)
        print("add_data:", i)
        time.sleep(0.2)
    pass


def read_data():
    print("read_data:", q_list)
    pass


if __name__ == '__main__':
    # 创建添加数据线程
    add_data_thread = threading.Thread(target=add_data)
    # 创建读取数据线程
    read_data_thread = threading.Thread(target=read_data)

    # 启动线程执行任务
    add_data_thread.start()
    # time.sleep(1)
    # 线程等待，主线程等待添加数据线程执行完成以后，代码再继续往下执行
    add_data_thread.join()
    read_data_thread.start()
    pass
