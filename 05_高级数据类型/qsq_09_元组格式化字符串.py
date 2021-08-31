info_tuple = ("小明", 21, 1.85 )
# 格式化字符串后面的‘()’本质上就是元祖
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple  # 用元祖可以拼接一个新的字符串

print(info_str)
