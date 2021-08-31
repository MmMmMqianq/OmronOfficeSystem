# 1. 字典的定义
# · dictionary（字典）是除列表外 python 之中最灵活的数据类型
# · 字典同样可以用来存储多个数据，通常用于存储 描述一个物体的相关信息
# · 和列表的区别：① 列表是有序的对象集合；② 字典时无序的对象集合
# · 字典用{}大括号定义
# · 字典是使用 键值对 存储数据，键值对之间使用逗号分隔
#     ① 键 key 是索引
#     ② 值 value 是数据
#     ③ 键和值之间使用：冒号分隔
#     ④ 键必须是唯一的
#     ⑤ 值可以是任意数据类型，但键只能用字符串、数字、或者元组

# 字典是一个无序的数据集合，使用print函数输出字典时，通常
# 输出的书序和定义的顺序是不一致的！
xiaoming_dict = {"name": "xiaoming",
            "age": 18,
            "height": 1.85,
            "weight": 75.5}
print(xiaoming_dict)

# 1. 字典的取值
print(xiaoming_dict["name"])  # 如果取值的时候 key 不存在会报错

# 2. 增加/修改
xiaoming_dict["gender"] = True  # 如果key在字典中不存在的话就会在字典中新添加一个
xiaoming_dict["name"] = "小小明"  # 如果key存在的就会修改key值
print(xiaoming_dict)

# 3. 删除
xiaoming_dict.pop("name")  # 如果指定的key存在就会报错
print(xiaoming_dict)