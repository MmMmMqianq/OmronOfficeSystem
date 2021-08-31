#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：test.py
时间：2021/06/22
"""
import socket

print('1.txt. ', socket.gethostname())  # 返回主机名
print('2. ', socket.gethostbyaddr('192.168.10.107'))  # 返回(hostname, aliaslist, ipaddrlist)，aliaslist为备用主机名；
print('3. ', socket.gethostbyname('oct-jq-sqqian1'))
print('4. ', socket.gethostbyname_ex(socket.gethostname()))

socket.setdefaulttimeout(2.0)  # 设置Socket默认超时时间；
socket.getdefaulttimeout()  # 获取socket默认超时时间；

