#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：10-1.txt.py
时间：2021/06/10
"""
file = open('data.txt', 'r')
print(type(file))  # <class '_io.TextIOWrapper'>
file.seek(6)  # 移动光标
print(file.read(6))  # 光标会自动移动到第五个字符后面
file.seek(0)
print(file.readline(), end='')  # 每一行本身会带有一个换行符(\n)，所以end=‘’，否则读出来的文本中间会多空一行
lines = file.readlines()
print(file)
for line in lines:
    print(line, end='')
file.close()  # 打开文件后一定要关闭，否则可能会出现意想不到的问题，占用系统资源
              # 一般要使用异常处理，ch10.close()写到finally里


with open('data.txt', 'r') as file1:  # 用with  as:的语法可以避免文件打开后忘记关闭的问题，执行完会自动关闭文件
    data = file1.readlines()
    print(data)
