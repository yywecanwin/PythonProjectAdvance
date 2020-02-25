# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/25

 # 1.导入进程multiprocessing包
import multiprocessing
import time
import os

def dance():
    # 扩展：获取当前代码的进程对象
    dance_process = multiprocessing.current_process()
    print("dance_process:",dance_process)
    # 获取当前进程（子进程）编号
    dance_pid = os.getpid()
    print("dance_pid",dance_pid)
    # 获取当前进程的父进程编码
    p_pid = os.getppid()
    print("dance_process的父进程编号：",p_pid)


    for i in range(3):
        print("跳舞中。。。。。")
        time.sleep(0.2)
        pass

    pass

def sing():
    for i in range(3):
        print("唱歌中。。。。。")
        time.sleep(0.2)
        pass

if __name__ == '__main__':

    #扩展：获取当前代码的进程对象
    main_process = multiprocessing.current_process()
    print("main：",main_process)
    # 获取当前进程（主进程）的编号
    main_pid = os.getpid()
    print("main_pid:",main_pid)


    # 2.创建进程对象
    # group:进程组，目前只能使用None，一般不要管他
    # target：指定执行的任务名
    # name：进程名，如果不指定默认的命名格式:process-1,....
    sub_process1 = multiprocessing.Process(target=dance,name="sub_process1")
    sub_process2 = multiprocessing.Process(target=sing,name="sub_process2")
    print("sub_process1:",sub_process1)
    print("sub_process2:",sub_process2)


    # 3.启动进程执行对应的任务
    sub_process1.start()
    sub_process2.start()
    pass







