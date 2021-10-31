#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：10-3.py
时间：2021/06/11
"""

with open('data_write', 'w+') as file:  # w打开的方式打开之前都会先将文件清空，用a的方式打开文件是从末尾追加
    # data1 = 'one two three'
    # file.write(data1+'\n')
    # data2 = '1.txt 2 3'
    # file.write(data2+'\n')

    data3 = ['one two three', '1.txt, 2, 3']
    # file.writelines(data3)  # 这种方法写入的数据不会自动换行

    # file.writelines([data+'\n' for data in data3])  # 这种写法最后会多出一个空行
    file.writelines('\n'.join(data3))  # 推荐这种写法和下面的写法
    # file.write('\n'.join(data3))

with open(r'C:\Users\sqqian.GC\Desktop\1.txt', 'w+', buffering=-1) as file1:  # buffering=1时，t模式：行缓冲，遇到换行符才flush,only usable in text mode
                                                                             # buffering=0时，b模式：关闭缓存区；t模式不支持关闭缓存区,only allowed in binary mode
                                                                             # buffering>1时，固定缓存区大小，缓存区满了才会将数据写到磁盘；
                                                                             # buffering=-1.txt(default)，使用默认的缓存区大小，缓存区满了才会将数据写到磁盘
    file1.write(input('输入：')+'\n')
    # file1Action.flush()  # 立即刷新，缓存里的数据会立刻写到磁盘；
    input('请输入：')

