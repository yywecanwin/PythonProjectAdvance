# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

# 1.导入线程的包
import threading
import time


# 跳舞任务函数
def dance():
    for i in range(3):
        print("唱歌中。。。。")
        time.sleep(0.2)
        pass

    pass


def sing():
    for i in range(3):
        print("唱歌中。。。。")
        time.sleep(0.2)

        pass

    pass


if __name__ == '__main__':
    # 2.创建线程的对象
    # group:表示线程组，目前只能使用None
    # target:表示执行任务名（函数名或者方法名）
    sub_thread1 = threading.Thread(target=dance)
    print(sub_thread1, sub_thread1.name)  # <Thread(Thread-1, initial)> Thread-1

    sub_thread2 = threading.Thread(target=sing)
    print(sub_thread2, sub_thread2.name)  # <Thread(Thread-2, initial)> Thread-2

    # 3.启动线程执行对应的任务
    sub_thread1.start()
    sub_thread2.start()

    pass
