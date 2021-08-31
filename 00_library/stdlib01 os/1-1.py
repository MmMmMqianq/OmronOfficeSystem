#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：2-1.txt.py
时间：2021/06/22
"""

import os

"""
1.txt. 系统相关变量操作；
2. 文件和目录相关操作；
3. 执行命令和管理进程
"""

# 1.txt. 系统相关变量操作
print(os.name)  # 当前的操作系统，nt表示windows
print(os.environ)  # windows下的环境变量
print(os.sep)  # 文件名分隔符，windows下为'\'
print(os.pathsep)  # path之间的分隔符，windows下为';'
print(os.linesep)  # 换行符，windows下为'\r\n'

# 2. 文件和目录相关操作
# os.mkdir('stddemo1')  # 也可使用绝对路径创建目录，但是目录的路径必须是已经存在的
# os.makedirs(r'C:\Users\sqqian.GC\Desktop\Python\Python\stdlib01 os\stddemo2\stddemo2_1')  # 创建多级目录，路径中目录不存在会自动创建

# os.rmdir('stddemo1')  # 也可使用绝对路径删除目录，但是目录的路径必须是已经存在的
# os.removedirs(r'C:\Users\sqqian.GC\Desktop\Python\Python\stdlib01 os\stddemo2\stddemo2_1')  # 递归删除目录，如果不是空目录则停止删除

print(os.stat('stddemo1'), '\n',  type(os.stat('stddemo1')))  # 获取文件的状态，包括大小、修改时间、上一次打开时间、创建时间等等；

print(os.getcwd())  # 返回表示当前工作目录的字符串

# os.path
file = os.getcwd() + r'\1.txt-1.txt.py'
print(os.path.split(file))  # 将目录和文件分离为一个元祖
print(os.path.isabs(file))  # 判断是否为绝对路径
print(os.path.isabs('1-1.py'))

# 相关判断
print(os.path.isdir(file))  # 是否为目录
print(os.path.isfile(file))  # 是否为文件
print(os.path.exists(file))  # 路径是否存在，在创建或者删除目录时可以先用os.path.exists()判断

# 获取文件的相关属性
print(os.path.getatime(file))  # 获取文件/目录上一次的访问时间，返回一个时间戳
print(os.path.getctime(file))  # 获取文件/目录的创建时间，返回一个时间戳
print(os.path.getmtime(file))  # 获取文件/目录的修改时间，返回一个时间戳
print(os.path.getsize(file))  # 获取文件/目录的大小，返回字节数

# 执行命令和进程管理
os.system('hello.py')  # 运行可执行文件
os.system('ipconfig')
