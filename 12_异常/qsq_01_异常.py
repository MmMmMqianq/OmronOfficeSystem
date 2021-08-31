"""
异常的概念：
1.程序运行时，如果Python解释器遇到一个错误，会停止程序运行，并且提示一些错误信息，这个就是异常；
2.程序停止 执行并且提示错误信息这个额动作，我们通常称之为：抛出(raise)异常；

捕获异常语法：
try:
    尝试执行代码
except：
    出现错误的处理

注意：如果尝试没有成功会执行except，然后程序继续往下执行并不会报错停止；
"""

try:
    # 不能确定能否正确执行代码，比如如果用户输入了一个字母，那么下面的代码是不会执行的，并且报错；
    num = int(input("请输入一个数字："))
except:
    # 出现错误后执行的代码
    print("请输入一个正确的整数")
print("-" * 50)
