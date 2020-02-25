# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/25

# 1.导入进程multiprocessing包
import multiprocessing
import time

def dance():
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

    # dance()
    # sing()

    # 2.创建进程对象
    # group:进程组，目前只能使用None，一般不要管他
    # target：指定执行的任务名
    sub_process1 = multiprocessing.Process(target=dance)
    sub_process2 = multiprocessing.Process(target=sing)


    # 3.启动进程执行对应的任务
    sub_process1.start()
    sub_process2.start()
    pass



