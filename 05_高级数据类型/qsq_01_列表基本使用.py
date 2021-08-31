# 1. 列表的定义
# List（列表） 是 Python 中使用 最频繁 的数据类型，在其他语言中通常叫做 数组
# 专门用于存储 一串 信息
# 列表用 [] 定义，数据 之间使用 , 分隔
# 列表的 索引 从 0 开始。在列表中取数据时，如果超过了索引的范围，程序就会报错
# 索引就是数据在 列表 中的位置编号，索引 又可以被称为 下标

# 2. 应用场景
# 尽管 Python 的 列表 中可以 存储不同类型的数据，但是在开发中，更多的应用场景是:
# 1> 列表 存储相同类型的数据
# 2> 通过 迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作

#
# 3. 列表常用操作
#
# 在 ipython3中定义一个列表，例如：name_list = []输入name_list.按下TAB键，ipython会提示列表能够使用的方法如下：
# In [1]: name_list.
# name_list.append   name_list.count    name_list.insert   name_list.reverse
# name_list.clear    name_list.extend   name_list.pop      name_list.sort
# name_list.copy     name_list.index    name_list.remove
#
# 序号 	分类 	关键字 / 函数 / 方法 	    说明
# 1 	增加 	 列表.insert(索引, 数据) 	在指定位置插入数据
# 		         列表.append(数据) 	    在末尾追加数据
#                列表.extend(列表2) 	    将列表2 的数据追加到列表
# 2 	修改     列表[索引] = 数据     	修改指定索引的数据
# 3 	删除 	 del 列表[索引] 	        删除指定索引的数据
# 		         列表.remove[数据]       	删除第一个出现的指定数据
# 		         列表.pop 	            删除末尾数据
# 		         列表.pop(索引) 	        删除指定索引数据
# 		         列表.clear 	            清空列表
# 4 	 统计 	 len(列表) 	            列表长度
# 		         列表.count(数据) 	    数据在列表中出现的次数
# 5   	 排序 	 列表.sort() 	        升序排序
# 		         列表.sort(reverse=True) 降序排序
# 		         列表.reverse() 	        逆序、反转

name_list = ["张三", "李四", "王五"]
# 1. 取值和索引 list[索引值]
# list index out of range - 列表的索引值超出范围
print(name_list[2])

# 知道内容想要知道在列表中的位置 list.index()
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("李四"))

# 2. 修改
name_list[1] = "孙六"
print(name_list[1])
# name_list[3] = "王小二" - 这样会报错：list assignment（指定） index out of range

# 3. 增加
name_list.append("李七")  # appand 方法可以向列表的末尾追加数据
name_list.insert(1, "小妹妹")  # inser 方法可以在列表指定的索引位置插入数据

name_list_temp = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(name_list_temp)  # extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾

print(name_list)

# 4. 删除
name_list.remove("王五")  # remove 方法可以可以从列表中删除 指定的 数据。如果元素出现多次则删除第一个
name_list.pop()  # pop 方法 默认 可以把列表的最后一个元素删除
name_list.pop(3)  # pop 方法可以指定要删除元素的索引，从而删除元素，同时 返回 删除的元素
name_list.clear()  # clear 方法可以清空列表中的所有元素

