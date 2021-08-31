# 字符串--判断型方法
# 1. 字符串中只包含空格，则返回True
str_space = " "
print("1.\t%s 中是否只包含加空格：%s" % (str_space, str(str_space.isspace())))

# 2. 字符串至少有一个字符并且所有字符都是数字或者字母，则返回True
str_num1 = "1234"
str_alpha1 = "abcd"
print("\n2.\t%s 只包含数字：%s\n\t%s 只包含字母：%s" % (str_num1, str(str_num1.isspace()),
                                    str_alpha1, str(str_alpha1.isspace())))

# 3. 字符串中包含的所有字符都是字母，则返回True
str_alpha2 = "alpha"
print("\n3.\t%s 只包含字母：%s" % (str_alpha2, str(str_alpha2.isalpha())))

# 4. 字符串中只包含数字，则返回True
str_num2 = "123"
print("\n4.\t%s 只包含数字：%s, %s, %s" % (str_num2, str(str_num2.isdecimal()),
                                 str(str_num2.isdigit()),
                                     str(str_num2.isnumeric())))

# 5. 字符串是标题化的（每个人单词的首字母是大写），则返回True
str_title = "This Is Title"  # 单词之间必须要有空格
print("\n5.\t%s 是否是标题：%s" % (str_title, str(str_title.istitle())))

# 6. 字符串中至少包含一个字母并且所有字母均为小写，则返回True
str_lower = "acbde"
print("\n6.\t%s 是否均为小写字母：%s" % (str_lower, str(str_lower.islower())))

# 7. 字符串中至少包含一个字母并且所有字母均为大写，则返回True
str_upper = "ABCDE"
print("\n7.\t%s 是否均为大写字母：%s" % (str_upper, str(str_upper.isupper())))
