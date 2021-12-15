"""
xlrd的使用：读取Excel的数据

1. xlrd常用函数
2. xlrd操作Excel行
3. xlrd操作Excel列
4. xlrd操作Excel单元格
"""
import xlrd

# 1. xlrd常用函数
workbook = xlrd.open_workbook("demo.xls")  # 返回工作簿对象
# workbook.sheet_loaded(0)  # 判断是否加载了工作表，可以指定工作表索引或者工作表名字
# workbook.unload_sheet(1)  # 卸载工作表，可以指定工作表索引或者工作表名字

print("1. ", workbook.sheets())  # 返回工作簿中的所有工作表列表
print("2. ", workbook.sheets()[0])  # 通过列表索引访问工作表
print("3. ", workbook.sheet_by_index(1))  # 通过工作索引访问工作表
print("4. ", workbook.sheet_by_name("Sheet3"))  # 通过名字访问工作表

print("5. ", workbook.sheet_names())  # 返回所有工作表的名字
print("6. ", workbook.nsheets)  # 返回工作表的数量


# 2. xlrd操作Excel行
sheet1 = workbook.sheet_by_index(0)  # 获取第一个工作表
print("7. ", sheet1.nrows)  # 获取第一个工作表下的有效行数
print("8. ", sheet1.row(1))  # 返回指定行单元格对象组成的列表
print("9. ", sheet1.row_types(1))  # 返回行所有的数据类型, 0：空字符串，1：字符串，2：浮点数，3：date，4:bool
print("10. ", sheet1.row(1)[0].value)  # 返回单元格对象的值
print("11. ", sheet1.row(1)[0].ctype)  # 返回单元格对象的数据类型
print("12. ", sheet1.row_values(1))  # 返回指定行的所有单元对象的值组成的列表
print("13. ", sheet1.row_len(1))  # 获取指定行的有效长度

# 3. xlrd操作Excel列
print("14.", sheet1.ncols)  # 获取第一个工作表下的有效列数
print("15.", sheet1.col(0))  # 返回指定列单元格对象组成的列表
print("16.", sheet1.col_types(0))  # 返回列所有的数据类型, 0：空字符串，1：字符串，2：浮点数，3：date，4:bool
print("17.", sheet1.col(0)[0].value)  # 返回单元格对象的值
print("18.", sheet1.col(0)[0].ctype)  # 返回单元格对象的数据类型
print("19.", sheet1.col_values(0))  # 返回指定列的所有单元对象的值组成的列表

# 4. xlrd操作Excel单元格
print("20, ", sheet1.cell(1, 0))  # 获取指定单元格
print("21. ", sheet1.cell_type(1, 0))  # 获取指定单元格内容数据类型
print("22. ", sheet1.cell(1, 0).ctype)  # 获取指定单元格内容数据类型
print("23. ", sheet1.cell_value(1, 0))  # 获取指定单元格的内容
print("24. ", sheet1.cell(1, 0).value)  # 获取指定单元格的内容
