# 字符串--文本对齐方法

# 1. 返回一个原字符串左对齐，并且使用fillchar填充至长度width的新字符串
# string.ljust(width[,fillchar])
# 注意：fillchar的长度必须是一个字符的长度
str1 = "qsqqwe"
print("1.\t %s 字符串左对齐：%s" % (str1, str1.ljust(10)))

# 2. 返回一个原字符串右对齐，并且使用fillchar填充至长度width的新字符串
# string.rjust(width[,fillchar])
# 注意：fillchar的长度必须是一个字符的长度
str2 = "qsqqwe"
print("\n2.\t %s 字符串右对齐：%s" % (str2, str2.rjust(10)))
print("\n2.\t %s 字符串右对齐,用12填充：%s" % (str2, str2.rjust(10, "1")))

# 3. 返回一个居中的原字符串，并且使用空格填充至长度width的新字符串
# 注意：①如果width小于原字符串长度，则直接返回原字符串
#      ②如果原字符串长度为偶数，width为奇数，则返回的字符串靠左一个字符居中
# string.center(width[,fillchar])
str3 = "1234567"
print("\n3.\t %s 字符串居中对齐：%s" % (str3, str3.center(5)))