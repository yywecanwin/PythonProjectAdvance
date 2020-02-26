# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading

# 定义全局变量
g_num = 0


# 循环1000000次：每循环一次结合全局变量加1
def calc_num1():
    # 声明此处加上global表示修改全局变量的内存地址
    global g_num
    for i in range(1000000):
        g_num += 1
        pass
    print("calc_num1:", g_num)

    pass


# 循环1000000次：每循环一次结合全局变量加1
def calc_num2():
    # 声明此处加上global表示要修改全局变量的内存地址
    global g_num
    for i in range(1000000):
        g_num += 1
        pass
    print("calc_num2:", g_num)

    pass


if __name__ == '__main__':
    # 创建第一个子线程
    first_thread = threading.Thread(target=calc_num1)
    # 创建第二个子线程
    second_thread = threading.Thread(target=calc_num2)

    # 启动线程执行任务
    first_thread.start()
    # 主线程等待第一个子线程执行完成以后程序再执行（线程同步）
    first_thread.join()
    second_thread.start()

    pass
