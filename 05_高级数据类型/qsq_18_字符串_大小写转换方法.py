# 字符串--大小写转换方法

# 1. 把字符串的第一个字母大写
# string.capitalize()
str1 = "abcde"
print("1.\t%s 首字母大写后的字符为：%s" % (str1, str1.capitalize()))

# 2. 把每个单词的首字母大写
# string.title()
str2 = "this is title"
print("\n2.\t%s 转换为标题：%s" % (str2, str2.title()))

# 3. 把所有字符转换为小写
# string.lower()
str3 = "123aBc一二三"
print("\n3.\t%s 所有字符转换为小写：%s" % (str3, str3.lower()))

# 4. 把所有字符转换为大写
# string.upper()
str4 = "123aBcQwerw一二三"
print("\n4.\t%s 所有字符转换为大写：%s" % (str4, str4.upper()))

# 5. 把字符串里的所有字符反转
# string.swapcase()
str5 = "123aBcQwerw一二三"
print("\n5.\t%s 所有字符反转：%s" % (str5, str5.swapcase()))

