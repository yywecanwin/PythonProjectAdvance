# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/26

import threading
import time


def task():
    for i in range(10):
        print("任务执行中。。。")
        time.sleep(0.3)
        pass

    pass


if __name__ == '__main__':
    # 创建子线程
    # 1.daemon=True 表示守护主线程，主线程退出子线程销毁
    # sub_thread = threading.Thread(target=task,daemon=True)

    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)

    # 启动线程执行任务
    sub_thread.start()

    time.sleep(1)
    print("主线程over")

    # 总结：
    """
        默认情况下，主线程会等待所有的子线程执行完成以后主线程退出
        
        解决方法：
            1.守护主线程：aemon=True 
            2.销毁线程：setDaemon(True)
            
    """

    pass
