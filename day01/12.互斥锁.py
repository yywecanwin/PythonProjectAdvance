# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading

# 定义全局变量
g_num = 0
# 创建互斥锁, 本质上是一个函数
lock = threading.Lock()

# 循环1000000次，每循环一次给全局变量加1
def calc_num1():
    # 操作共享数据之前，要上锁
    lock.acquire()
    # 声明此处加上global表示要修改全局变量的内存地址
    global g_num
    for i in range(1000000):
        g_num += 1

    print("calc_num1:", g_num)
    # 共享数据操作完成以后，需要释放锁
    lock.release()
# 循环1000000次，每循环一次给全局变量加1
def calc_num2():
    # 操作共享数据之前，要上锁
    lock.acquire()
    # 声明此处加上global表示要修改全局变量的内存地址
    global g_num
    for i in range(1000000):
        g_num += 1

    print("calc_num2:", g_num)
    # 共享数据操作完成以后，需要释放锁
    lock.release()
if __name__ == '__main__':
    # 创建第一个子线程
    first_thread = threading.Thread(target=calc_num1)
    # 创建第二个子线程
    second_thread = threading.Thread(target=calc_num2)
    # 启动线程执行任务
    first_thread.start()
    second_thread.start()

    # 结论: 互斥锁可以解决全局变量数据错误问题，互斥锁可以保证同一时刻只有一个线程取值

    # 性能: 执行代码的效率会下降，能够保证数据的安全性