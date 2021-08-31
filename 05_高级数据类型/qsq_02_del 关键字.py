name_list = ["张三", "李四", "王五"]

# (知道)使用del关键字（delete）删除列表元素
# 在日常开发中，要从列表中删除数据，建议使用列表提供的方法
del name_list[1]
print(name_list)

# del 关键字本质上使用来将一个变量从内存中删除的，例如：
name = "小红"
del name  # 删除之后name变量就不能再使用了，因为被 del 从内存删除了
# print(name) 执行这条命令时会提示name变量未定义
