#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：1.txt-1.txt.py
时间：2021/06/29
"""

import json

data1_dict = {'a': 'Hello', 'b': 123, 'c': [1, 2, 3]}
data1_str = json.dumps(data1_dict)
print(data1_str, type(data1_str))

data2_str = '{"a": "hello", "b": 123, "c": [1.txt, 2, 3]}'
# data2_str = "{'a': 'Hello', 'b': 123, 'c': [1.txt, 2, 3]}"
data2_dict = json.loads(data2_str)
print(data2_dict, type(data2_dict))
