"""
1.一个独立的Python文件就是一个模块；
2.在导入文件时，文件中的所有没有任何缩进的代码都会被执行一遍；

应用场景：代码只需在当前模块中执行，而被导入到其他文件中不需要执行；
__name__，在当前的模块里执行__name__输出的永远是"__main__"，在调用这个模块的程序里输出的就是这个模块的名字；

在很多Python文件中都会看到以下格式的代码：
# 导入模块
# 定义全局变量
# 定义类
# 定义函数

# 在代码的最下方
def main():
	# ...
	pass

# 根据__name__判断是否执行下方代码
if __name__ == "__main__"
	main()
"""


def __test_():
	print("我是测试函数！")


# 在当前的模块里执行__name__输出的永远是__main__，在调用这个模块的程序里输出的就是这个模块的名字；
print(__name__)


def main():
	__test_()


# 在模块内部通过判断__name__是否等于__main__来决定模块里的代码是否在调用该模块的代码里执行；
if __name__ == "__main__":
	main()
