# 字符串、列表、元祖切片基本语法: 字符串[开始索引, 结束索引, 步长]  步长不能为0，不写默认为1
# 注意：字典不能，字典里的键值对是无序的
str1 = "0123456789"
print(str1[0:5:1])  # 输出结果为'01234'
print(str1[0:5:2])  # 输出结果为'024'
print(str1[0:9:3])  # 输出结果为'036'
print(str1[0:-2:3])  # 输出结果h和上一条是一样，-2是倒序的索引值，和9索引的是同一个位置

