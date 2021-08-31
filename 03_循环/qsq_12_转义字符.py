# Python转义字符：
# \（在尾行时）：续行符
# \\：反斜杠符号
# \'：单引号
# \"：双引号
# \a：响铃
# \b：退格
# \000：空
# \n：换行
# \v：纵向制表符
# \t：横向制表符
# \r：回车
# \f：换页
# \oyy：八进制数
# \xyy：十六进制数
# \other：其他的字符以普通格式输出

# \（在结尾）：续行符
print("abcddfsdfsdfsdfsdfs\
adfg")  # 当一行不够写是可以在结尾加一个反斜杠续行

# \000：空
print("aaa\000")


# \\：反斜杠符号
print("abc\\abc")  #abc中间会输出 \

# \a：响铃
print("abc\a")  # 输出abc的同时还会有一声响铃
print("\a")

# \b：退格
print("aaa\b")  # 会自动删除一个字符，输出aa，而不是aaa


# \t 制表符：在不使用表格的情况下 在垂直方向 按列对齐。
# 一个\t就会输出4个空格及一个制表符（Tab）的长度
print("a\tab\tabc\tabcd\tabcde\t")
# a\t    输出的结果是 a    后面3个空格
# ab\t   输出的结果是 ab   后面2个空格
# abc\t  输出的结果是 abc  后面1个空格    字符长度小于4时，\t制表符会转换为4-字符长度个空格
# abcd\t 输出的结果是 abcd 后面4个空格    字符长度等于4时，\t制表符会转换为4个空格
# abcde\t输出的结果是 abcde后面3个空格    字符长度大于4时，\t制表符会转换为4-（字符长度-4）个空格
print("a\tab\tabc\tabcd\tabcdefg\ta")
print("a\tddd\tsdsdas\t\tdas\t\ta")  # 两个print函数输出的字符是垂直方向是对齐的

# \n 在控制台输出一个 换行符
print("HELLO Python")  # 输出在一行
print("HELLO\nPython")  # 输出在两行
