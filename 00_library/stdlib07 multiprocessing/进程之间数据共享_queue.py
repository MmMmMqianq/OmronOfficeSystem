#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：进程之间的通信.py
时间：2021/12/29

Queue:
    队列是在运行内存里分配一定内存大小用于进程/线程间的数据共享；
    详细看官方文档
"""
import multiprocessing
import threading

def download_data(q: multiprocessing.Queue):
    # 假设data为下载先来的数据
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    for temp in data:
        if q.full():  # q.full()用于判读队列是否满了
            break
        else:
            q.put(temp)
    print("------数据已经全部放到了队列中------")


def anaisys_data(q: multiprocessing.Queue):
    # 获取队列的的数据
    get_data = list()
    while True:
        if q.empty():  # q.empty()用于判读队列是否为空
            break
        else:
            get_data.append(q.get())
    print("获取到的数据为get_data = ", get_data)


if __name__ == "__main__":
    q = multiprocessing.Queue(3)  # 不指定大小默认会根据运行内存大小自动分配

    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p2 = multiprocessing.Process(target=anaisys_data, args=(q, ))
    p1.start()
    p2.start()