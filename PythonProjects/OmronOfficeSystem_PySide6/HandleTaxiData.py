"""
HandleTaxiData模块说明：
Excel数据读取方法；
Excel数据写入方法；
生成随机金额并且写入到Excel方法；
Excel里增加姓名方法；
"""

import random
import pandas
from pandas import DataFrame
import numpy


# def random_invoice_amount(name):
#     taxi_excel = pandas.read_excel('Taxi.xlsx')
#     # print(dict(taxi_excel.values))
#     taxi_dict = dict(taxi_excel.values)
#     if name != "":
#         taxi_dict.update({name: 0})
#     taxi_data = []
#     old_name_list = []
#     money_list = []
#     for key in taxi_dict:
#         money = random.randint(350, 399)
#         taxi_temp = [key, money]
#         taxi_data.append(taxi_temp)
#         old_name_list.append(key)
#         money_list.append(money)
#     print(taxi_data)
#     taxi_df = DataFrame(taxi_data, columns=["姓名", "金额"])
#     taxi_df.to_excel("Taxi.xlsx", index=False, header=True, sheet_name="sheet1")
#     return old_name_list, money_list
    # print(taxi_excel.index)
    # print(taxi_excel.index.stop)
    # print(taxi_excel.values[0][1])
    # print(taxi_excel['名字'].values)
    # print(taxi_excel['金额'].values)
    # money_list = []
    # old_name_list = taxi_excel['姓名'].values
    # i = 0
    # for key in taxi_dict:
    #     money = random.randint(350, 399)
    #     # money_list.append(money)
    #     taxi_excel['金额'].values[i] = money
    #     i += 1
    # # print(taxi_excel['金额'].values)
    # DataFrame(taxi_excel).to_excel('taxi.xlsx', sheet_name='sheet1', index=False, header=True)
    # return old_name_list, taxi_excel['金额'].values


def read_excel():
    taxi_excel = pandas.read_excel('Taxi.xlsx')

    # 检查Excel表格内"姓名"列是否有NaN值，有的话将其所在的行剔除
    isnan_df = taxi_excel.isnull()
    for i in range(0, isnan_df.index.stop):
        if bool(isnan_df["姓名"].values[i]):
            taxi_excel_drop = taxi_excel.drop([i, ])
            taxi_excel = taxi_excel_drop

    # 将"金额"列的NaN填充为0
    taxi_excel_temp = taxi_excel.fillna(0)

    # 将DataFrame的数据转换为列表形式并返回
    taxi_dict = dict(taxi_excel_temp.values)
    taxi_data_list = []
    for key in taxi_dict:
        taxi_data_list.append([key, int(taxi_dict[key])])
    return taxi_data_list


def write_excel(taxi_data):
    taxi_df = DataFrame(taxi_data, columns=["姓名", "金额"])
    taxi_df.to_excel("Taxi.xlsx", index=False, header=True, sheet_name="sheet1")


def append_name(name):
    taxi_data = read_excel()
    if name != '':
        taxi_data.append([name, 0])
    write_excel(taxi_data)


def random_invoice_amount(upper_limit=400, lower_limit=350):
    taxi_data = read_excel()
    taxi_data_temp = []
    if upper_limit < lower_limit:
        limit_temp = int()
        limit_temp = upper_limit
        upper_limit = lower_limit
        lower_limit = limit_temp
    for i in range(len(taxi_data)):
        money = random.randint(lower_limit, upper_limit)
        taxi_data_temp.append([taxi_data[i][0], money])
    taxi_data = taxi_data_temp
    write_excel(taxi_data)


if __name__ == "__main__":
    import time
    print(read_excel())
    # time.sleep(3)
    append_name("小时")
    print(read_excel())
    random_invoice_amount()
    print(read_excel())

