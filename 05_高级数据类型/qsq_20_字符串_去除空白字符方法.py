# 字符串--去处空白字符方法

# 1. 截掉字符串左边的空白字符
#  string.lstrip()
str1 = "  abcdef  "
print("1.\t %s 去除字符串左边的空白字符：%s" % (str1, str1.lstrip()))

# 2. 截掉字符串右边的空白字符
#  string.rstrip()
str2 = "  abcdef  "
print("\n2.\t %s 去除字符串右边的空白字符：%s" % (str2, str2.rstrip()))

# 3. 返回删除前导和尾随字符的字符串的副本。chars参数是一个字符串，指定要删除的字符集。
#    如果省略或为None，则chars参数默认为删除空格。 chars参数不是前缀或后缀；而是删除其值的所有组合。
#  string.strip(char)
str3 = "www.baidu      .com"
print("\n3.\t %s 去除字符串中www..com字符：%s" % (str3, str3.strip("mwc .wo")))