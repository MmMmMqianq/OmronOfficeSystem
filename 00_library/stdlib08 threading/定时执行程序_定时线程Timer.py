import threading

"""
loop_execute_program(count, sec, fun)
循环执行fun，count为执行的次数，sec为时间间隔
"""


def b():
	print(2)


def loop_execute_program(count, sec, fun):
	"""
	:param count: 指定程序执行次数
	:param sec: 时间间隔
	:param fun: 循环执行的函数
	"""
	c = 0

	def a():
		threading.Timer(sec, function=a).start()
		nonlocal c
		if c > 0:
			fun()
		if c >= count:
			for i in threading.enumerate():
				if threading.enumerate().index(i) != 0:
					i.cancel()
			return
		c += 1
	a()


# b()循环执行5次，间隔1秒
loop_execute_program(5, 1, b)