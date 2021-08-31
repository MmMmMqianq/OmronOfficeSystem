name_list = ["张三", "李四", "王五", "王小二", "张三"]

# 使用迭代遍历列表；针对列表中的每一项元素，执行相同的操作
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在
my_name 这个变量中，在循环体内部可以访问到当前只一次获取到的数据

迭代遍历列表基本格式：
for my_name in 列表名称:
    print("我的名字叫 %s" % my_name)
"""

i = 0
for my_name in name_list:
    print("我的名字叫 %s" % my_name)
    name_list[i] = my_name + "HaHaHaHaHa"
    i += 1

print(name_list)
