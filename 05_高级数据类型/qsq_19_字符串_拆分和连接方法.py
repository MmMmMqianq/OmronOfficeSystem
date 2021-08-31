# 字符串--拆分和连接方法

# 1. 在第一次出现sep时分割字符串，并返回一个三元组，其中包含分隔符之前的部分，
#    分隔符本身以及分隔符之后的部分。 如果找不到分隔符，则返回一个包含字符串本
#    身的3元组，然后是两个空字符串('字符串本身', '', '',)。
# string.partition(sep)  sep:separator分离器
str1 = "1234abcd一二三四"
print("1.\t %s 以abcd把字符串分成一个三个元素的元祖：" % str1, str1.partition("abcd"))

# 2. 在最后一次出现sep时拆分字符串，并返回一个三元组，其中包含分隔符之前的部分，
#    分隔符本身以及分隔符之后的部分。 如果找不到分隔符，则返回一个包含两个空字符
#    串的三元组，然后是字符串本身('', '','字符串本身')。
# string.rpartition(sep)  sep:separator分离器
str2 = "1234abcd一二三四"
print("\n2.\t %s 以abcd，从左边开始查找，把字符串分成一个三个元素的元祖：" % str2, str2.rpartition("abcd"))

# 3. 使用sep作为分隔符字符串，返回字符串中单词的列表(list),如果sep不指定，那么以任意的空白字符分割。
#    如果指定了maxsplit，最多完成maxsplit个分割（因此，列表最多包含maxsplit + 1个元素）。
#    如果未指定maxsplit或-1，则分割数没有限制（进行所有可能的分割）。
# string.split(sep=none, maxsplit=-1)
str3 = "1,2,3,4,,5"
print("\n3.\t %s 以\",\"把字符串分成一个列表：" % str3, str3.split(sep=",", maxsplit=-1))

# 4.返回字符串中的行列表，在行边界处中断。 除非给出了keepends并且为true，否则换行符不包
#   含在结果列表中。
# unix换行：\n (0x0A)
# MAC回车：\r (0x0D)
# WIN回车换行：\r\n (0x0D,0x0A)
# string.spiltlines(keepends=False)  keepends默认为False
str4 = "a\r\nb\nc\rd"
print("\n4.\t字符串 %s 在行边界中断后得到的列表为：" % str4, str4.splitlines(keepends=False))
print("\n4.\t字符串 %s 在行边界中断后保留换行符得到的列表为：" % str4, str4.splitlines(keepends=True))

# 5. 返回一个字符串，该字符串是可迭代的字符串的串联。 如果有可迭代的任何非字符串值（包括字节对象），
#    则将引发TypeError。 元素之间的分隔符是提供此方法的字符串。
# string.join(iterable)
str5 = "abc"
print("\n5.\t %s 用\"-----\"迭代字符串串联" % str5, str5.join("-----"))