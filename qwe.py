#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：qwe.py
时间：2021/09/27
"""
import os

name_list = os.listdir(r"C:\Users\sqqian.GC\Desktop\1")
print(name_list)

i = 1
for name in name_list:
    new_name = "%d.jpg" % i
    path_old = "C:\\Users\\sqqian.GC\\Desktop\\1\\" + name
    path_new = "C:\\Users\\sqqian.GC\\Desktop\\1\\" + new_name
    os.rename(path_old, path_new)
    i = i + 1
