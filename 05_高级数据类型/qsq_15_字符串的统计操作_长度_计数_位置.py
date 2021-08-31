hello_str = "hello hello"

# 1. 统计字符串长度
len(hello_str)

# 2. 统计某一个字符串里的子字符串出现的次数
hello_str.count("llo")
hello_str.count("abc")  # 如果子字符串不存在则输出结果为0

# 3. 某个子字符串出现的位置
hello_str.index("llo")
hello_str.index("abc")  # 如果子字符串不存在程序会报错