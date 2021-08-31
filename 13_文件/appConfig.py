#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：appConfig.py
时间：2021/06/11
"""
config_data = {}
with open('app.config', 'r') as config_file:
    data = config_file.readlines()
    print(data)
    for line in data:
        # print(line)
        if line.startswith('#'):
            continue
        else:
            line = line.replace('\n', '')
            key = line.split(' = ', maxsplit=-1)[0]
            value = line.split(' = ', maxsplit=-1)[1]
            config_data[key] = value

if __name__ == '__main__':
    print(config_data)
