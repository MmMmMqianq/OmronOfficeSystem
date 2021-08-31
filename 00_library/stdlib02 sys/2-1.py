#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：2-1.txt.py
时间：2021/06/23
"""
# sys标准库主要是针对Python解释器相关的变量和方法

import sys

print(sys.version)  # Python版本号，一般如果对程序运行必须要为某个版本及以上时，可以用这个来判断
print(sys.maxsize)  # Python变量可以表示对的最大值
print(sys.path)  # 检索Python路径
print(sys.platform)  # Python运行的平台输出为 win32，os.names输出的是当前的操作系统，这两个是有本质区别
print(sys.copyright)  # Python版权
print(sys.argv)  # 参数

# sys.exit(0)  # 退出，可以设置状态码，默认为0
print(sys.getdefaultencoding())  # Python默认字符编码为UTF-8
print(sys.getfilesystemencoding())  # Python默认文件系统字符编码为UTF-8
print(sys.getrecursionlimit())  # Python默认的递归次数，默认为1000次，可以用sys.setrecursionlimit()更改
