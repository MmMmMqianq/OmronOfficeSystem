#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：进程池_pool.py
时间：2021/12/29

在任务很多，不确定任务个数时可以使用进程池
"""
import multiprocessing
import time


def fun(a):
    time.sleep(a)
    print(a)


if __name__ == "__main__":
    po = multiprocessing.Pool(3)  # 进程池数量

    # Pool().aooly_async(要调用的目标, (传递目标的参数元祖,))
    for i in range(10):
        po.apply_async(fun, (i,))  # 任务添加到线程池后立刻开始执行，如果超过了最大进程数则会放到缓存区等待空闲进程

    print("------start------")
    po.close()  # 关闭进程池，关闭后不在接收新的请求
    po.join()  # 等待进程池里的所有进程执行完毕，必须放在close()之后。如果不适用jion()的话主进程直接就结束了。
    print("------所有进程执行完毕------")
