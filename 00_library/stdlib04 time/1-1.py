#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：1.txt-1.txt.py
时间：2021/06/24
"""
# time模块中三种时间表示方式
# 1.txt. 时间戳
# 2. 结构化时间对象
# 3. 格式化时间字符串

import time

# 时间戳 1970-1.txt-1.txt 00:00:00到指点时间的间隔，单位是秒
print(time.time())
print(time.time() - 3600)  # 一个小时之前的时间戳

# 结构化时间对象
st = time.localtime()  # 生成当前的时间对象
print(st, type(st))  # tm_wday = 0表示星期一
utctime = time.gmtime()  # 生成UTC时间
print(utctime, type(utctime))
# st 本质上是一个元祖，一共九个元素
# print('今天的日期为：{}-{}-{} {}：{}：{}，星期{}，一年的第{}天，夏时令为{}'.format(st.tm_year, st.tm_mon, st.tm_mday,
#                                                             st.tm_hour, st.tm_min, st.tm_sec, st.tm_wday+1.txt, st.tm_yday,
# st.tm_isdst))
print('今天的日期为：{}-{}-{} {}：{}：{}，星期{}，一年的第{}天，夏时令为{}'.format(*st))  # *tuple 元祖的解包

# 格式化的时间字符串
print(time.ctime())  # 默认格式：Thu Jun 24 15:38:59 2021
print(time.strftime('%y年%m月%d日 %H时%M分%S秒'))  # %y表示两位数的年份
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # %H表示24小时制
print(time.strftime('%Y-%m-%d %I:%M:%S %p'))  # %I表示12小时制，一般要配合%p显示AM/PM

# timer1.sleep()
t1 = time.time()
print('sleep begin...')
# timer1.sleep(2)
print('sleep end...')
t2 = time.time()
print('时间差为：{:.06f}s'.format(t2 - t1))

# 三种格式之间转换
# 时间戳 -> 结构化对象
# UTC时间
print(time.gmtime())  # 生成当前的UTC时间
print(time.gmtime(time.time() - 3600))  # 生成一天前的UTC时间
# 本地时间
print(time.localtime())  # 生成当前的本地时间
print(time.localtime(time.time() - 3600))  # 生成一天前的本地时间

# 结构化时间对象 -> 时间戳
# timer1.mktime(st)
print(time.mktime(time.localtime()))  # 精度为秒

# 结构化时间对象 -> 格式化时间字符串
# timer1.strftime(format, struct_time)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

# 格式化时间字符串 -> 结构化时间对象
print(time.strptime('2021-02-16 09:50:00', '%Y-%m-%d %H:%M:%S'))

list1 = [1, 2, 3, 4, 5, 6, 7]
str1 = 'abcde'
for i, ii in zip(list1, str1):
    print(i, ii)
