info_tuple = ("张三", 18, 1.75, "张三")

# 取值 就是从 元组 中获取存储在指定位置的数据
# 遍历 就是 从头到尾 依次 从 元组 中获取数据

# 在Python中，可以使用 for 循环遍历所有非数字型类型的变量：列表、元组、字典 以及 字符串
# 提示：在实际开发中，除非能够确认元组中的数据类型，否则针对元组的循环遍历需求并不是很多

for my_info in info_tuple:

    # 使用格式字符串拼接 my_info 这个变量不方便！
    print(my_info)