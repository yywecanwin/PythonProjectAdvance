# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import multiprocessing
import time


def task():
    for i in range(3):
        print("正在工作中。。。。。")
        time.sleep(0.2)
        pass
    pass

if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 2.设置保护主进程，主进程退出子进程就销毁，停止运行
    sub_process.daemon = True

    # 启动子进程执行对应的任务
    sub_process.start()



    # 主进程延时0.3秒
    time.sleep(0.3)
    # 1.让子进程销毁
    # sub_process.terminate()
    print("主进程over。。。。")



    # 默认：主进程会等待所有的子进程执行完成以后主进程再退出

    #主进程不等待子进程的操作
    # 1.主进程等再 退出执行，先让子进程进行销毁，sub_process.terminate()
    # 2.设置守护主进程，主进程退出子进程直接销毁，不再执行子进程里面的任务

    pass




