# 打印分割线，分割线的内容和长度可变
def print_line(char, times):
    print(char * times)


print_line(input("输入字符："), int(input("输入次数：")))
