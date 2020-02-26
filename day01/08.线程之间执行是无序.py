# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading
import time


def task():
    time.sleep(0.2)

    # 获取当前线程名称
    print(threading.current_thread().name)

    pass


if __name__ == '__main__':
    my_list = []

    for i in range(10):
        sub_thread = threading.Thread(target=task)  # 添加列表
        my_list.append(sub_thread)

        pass

    # 循环速度是特别快的，等与让多个线程同时执行
    for value in my_list:
        value.start()
        pass

    pass
