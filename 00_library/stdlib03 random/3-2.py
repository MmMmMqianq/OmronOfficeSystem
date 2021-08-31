#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：3-2.py
时间：2021/06/23
"""
# 生成类似随机密码的字符串

# 要求：
# 1.txt. 密码要包含数字和大小写字母；
# 2. 可以指定密码位数；
import random
import string


def random_string(length):
    # 生成数字的随机长度
    number_count = random.randint(1, length-1)
    letter_count = length - number_count

    random_str = ''
    # simple1 = [i for i in range[0-10]]
    numbers = string.digits
    for _ in range(0, number_count):
        random_str += random.choice(numbers)

    letter = string.ascii_lowercase+string.ascii_uppercase
    for _ in range(0, letter_count):
        random_str += random.choice(letter)

    randomstrlist = []
    for randomstr1 in random_str:
        randomstrlist.append(randomstr1)

    random.shuffle(randomstrlist)

    randompassword = ''
    for randomstrlist1 in randomstrlist:
        randompassword += randomstrlist1
    return randompassword


if __name__ == '__main__':
    password = random_string(20)
    print(password)
