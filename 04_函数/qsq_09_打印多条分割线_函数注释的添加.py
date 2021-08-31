# 打印分割线，分割线的内容和长度可变
def print_lines(char, times, lines):
    """打印多行分割线

    :param char: 分割线使用的分割字符
    :param times: 每行分割线的字符数
    :param lines: 分割线行数
    """
    i = 1
    while i <= lines:
        print(char * times)
        i += 1


print_line(input("输入字符："), int(input("每行字符数：")), int(input("输入行数：")))

