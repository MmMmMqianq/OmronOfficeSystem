# 字符串--查找和替换方法

# 1. 用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
#    如果参数start和end指定值，则在指定范围内检查。
# string.startswith(prefix, start, end )  start默认为0，end默认为len(string)
str1 = "abcdefghijklmn"
print("1.\t%s 是否以ab开头：%s" % (str1, str(str1.startswith("ab"))))

# 2. 用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
#    可选参数"start"与"end"为检索字符串的开始与结束位置。
# string.endswith(suffix, start, end)   start默认为0，end默认为len(string)
str1 = "abcdefghijklmn"
print("\n2.\t%s 是否以f结尾：%s" % (str1, str(str1.endswith("ab"))))

# 3. 检查str是否在string中，如果start和end指定范围，则从左往右检查是否包含在指定范围内。
#    如果是返回开始索引值，否则返回-1
# string.find（str, start=0, end=len(string)） find()方法是不带关键字的参数，也就是说不能谢写为string.find（str, start=2, end=5）
str1 = "abcdefghijklmn"
print("\n3.\t%s 中在2-5的范围内是否包含de两个字符：%s" % (str1, str(str1.find("de", 2, 5))))
print("\t%s 中在2-5的范围内是否包含ed两个字符：" % str1, str1.find("ed", 2, 5))

# 4. 检查str是否在string中，如果start和end指定范围，则从右往左检查是否包含在指定范围内。
#    如果是返回开始索引值，否则返回-1
# string.rfind（str, start=0, end=len(string)） find()方法是不带关键字的参数，也就是说不能谢写为string.find（str, start=2, end=5）
str1 = "abcdefghijklmn"
print("\n4.\t%s 中在2-5的范围内是否包含de两个字符：%s" % (str1, str(str1.rfind("de", 2, 5))))
print("\t%s 中在2-5的范围内是否包含ed两个字符：%s" % (str1, str(str1.rfind("ed", 2, 5))))

# 5. 检查str是否在string中，如果start和end指定范围，则从左往右检查是否包含在指定范围内。
#    如果是返回开始索引值，否则程序会报错
# string.index（str, start=0, end=len(string)） find()方法是不带关键字的参数，也就是说不能谢写为string.find（str, start=2, end=5）
str1 = "abcdefghijklmn"
print("\n5.\t%s 中在2-5的范围内是否包含de两个字符：%s" % (str1, str(str1.index("de", 2, 5))))
# print("\t%s 中在2-5的范围内是否包含ed两个字符：%s" % (str1, str(str1.index("ed", 2, 5)))) 会报错substring not found

# 6. 检查str是否在string中，如果start和end指定范围，则从右往左检查是否包含在指定范围内。
#    如果是返回开始索引值，否则程序会报错
# string.rindex（str, start=0, end=len(string)） find()方法是不带关键字的参数，也就是说不能谢写为string.find（str, start=2, end=5）
str1 = "abcdefghijklmn"
print("\n6.\t%s 中在2-5的范围内是否包含de两个字符：%s" % (str1, str(str1.rindex("de", 2, 5))))
# print("\t%s 中在2-5的范围内是否包含ed两个字符：%s" % (str1, str(str1.rindex("ed", 2, 5)))) 会报错substring not found

# 7. 把字符串中的old_str替换成new_str，如果num指定，则替换不超过num次
# string.replace(old_str, new_str, num=string.count(old_str))
str2 = "abcdefghabijklmnabeabeabeab"
print("\n7.\t%s 中前三个ab字符替换为w后的新字符为：%s" % (str2, str2.replace("ab", "w", 3)))
