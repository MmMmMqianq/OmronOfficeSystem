#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：多任务_进程.py
时间：2021/12/29

多进程
1. 每创建一个进程在任务管理器里面都能看到；
2. 现有进程再有线程
"""
import multiprocessing
import time


def fun1(a, b):
    c = a + b
    time.sleep(10)
    print(c)
    return c


if __name__ == "__main__":
    i = 0
    while i < 5:
        p1 = multiprocessing.Process(target=fun1, args=(1, 2,))
        p1.start()
        i += 1
