# 1. 元组的定义
#
# Tuple（元组）与列表类似，不同之处在于元组的 元素不能修改,如果 修好元组里面的参数会报错：TypeError: 'tuple' object does not support item assignment
# ·元组 表示多个元素组成的序列
# ·元组 在 Python 开发中，有特定的应用场景
# ·用于存储 一串 信息，数据 之间使用 , 分隔
# ·元组用 () 定义
# ·元组的 索引 从 0 开始
# ·索引 就是数据在 元组 中的位置编号
#
# info_tuple = ("zhangsan", 18, 1.75)
#
# 创建空元组：info_tuple = ()
#
# 元组中只包含一个元素时，需要在元素后面添加逗号：info_tuple = (50, )
#
# 2.元祖的应用场景：
# 尽管可以使用 for in 遍历元祖，但是在开发中，更多的应用场景是：
# · 元祖可以作为 函数的参数和返回值，一个函数可以接受任意多个参数，或者返回多个参数；
# · 格式化字符串，格式化字符串后面的()本质上就是个元祖；
# 让列表不可以被修改，以保护数据安全；


info_tuple = ("张三", 18, 1.75, "张三")

# 1. 取值和取索引
print(info_tuple[1])
# 已经知道数据的内容，希望知道该数据在元祖中的索引
print(info_tuple.index("张三"))

# 2. 统计计数
count = info_tuple.count("张三")
print(count)

# 3. 元祖长度
print(len(info_tuple))