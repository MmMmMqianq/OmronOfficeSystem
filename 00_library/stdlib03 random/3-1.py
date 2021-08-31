#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：3-1.txt.py
时间：2021/06/23
"""
# random主要功能是生成伪随机数

import random

# 生成随机整数
print(random.randint(0, 100))  # 首尾都包含
# 在生成随机奇数或者偶数时用random.range()
print(random.randrange(1, 101, 2))  # 随机奇数，算头不算尾
print(random.randrange(2, 101, 2))  # 随机偶数

# 随机生成浮点数
print(random.random())  # 生成0.0-1.txt.0之间的随机数，一般可用于生成随机比例
print(random.uniform(11.2, 18.8))  # 生成任意范围的随机浮点数

# 非数字类型的随机抽样
targetList1 = ['a', 'b', 'c', 'e', 'f']
print(random.choice(targetList1))  # 随机抽一个样本
print(random.sample(targetList1, 2))  # 随机抽取多个样本，如果抽取的样本数等于样本总个数，那么也起到了乱序的作用，和random.shuffle()区别是random.sample()不会该本原序列
# 乱序
targetList2 = ['a', 'b', 'c', 'e', 'f']
random.shuffle(targetList2)  # random.shuffle()改变原列表，只能对列表乱序，不能对字符串乱序，可用于扑克牌洗牌
print(targetList2)           # 为什么不能乱序字符串，因为字符串是不可修改的，而random.shuffle()会修改原序列，所以无法乱序字符串，只能是列表

