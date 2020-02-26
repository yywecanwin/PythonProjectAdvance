# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading


# 创建互斥锁
lock = threading.Lock()


# 保证同一时刻只有一个线程根据下标去取值
def get_value(index):

    # 取值之前先上锁
    lock.acquire()
    my_list = [1, 4, 8]

    # 判断下标是否越界
    if index >= len(my_list):
        print("下标越界:", index)
        # 下标越界不能取值，也需要把锁释放，保证后面的线程可以再次取值
        lock.release()
        return

    # 根据下标获取值
    result = my_list[index]

    print(result)
    # 取值完成需要释放锁
    lock.release()


if __name__ == '__main__':
    # 创建很多线程，同时执行某个任务
    for i in range(5):
        # 创建子线程
        sub_thread = threading.Thread(target=get_value, args=(i,))
        # 启动线程执行任务
        sub_thread.start()

