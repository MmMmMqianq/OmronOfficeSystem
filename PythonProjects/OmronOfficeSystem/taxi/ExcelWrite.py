import logging.config
import random

import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


def random_number(a, b, maximum):
	"""
	思路：
	1. 参数：张数、总金额
	2. 在给定的范围里产生一个随机数列表
	3. 判断产生的随机数总和与给定的总和是否相等
		大于时，将差值除以随机数数量取商，每个随机数减去这个商值
			如果随机数减去商值要是超出范围，那么该值就为范围的最小值，剩下的值从随机数中的最大值减去
		再取差值除以随机数数量的模值，随机数从大到小的依次减1，如果随机数已经等于最小值，那么再从随机数中的最大值上减1
		小于时。。。思路同上

	函数功能：给定范围中间值、范围最大值，在该范围内取出a个随机数，随机数总和为范围中间值。
	:param a: a为生成随机数的个数
	:param b: 设定随机数的总和
	:param maximum: 每个随机数要<=maximum
	:return: 返回随机数列表n2_l，s2为随机数的总和，minimum为范围最小值
	"""
	average = b // a
	minimum = 2 * average - maximum
	n_l = list()  # 用于存储未经处理随机数
	# n_l = [36, 39, 22, 43, 24, 97]
	for _ in range(0, a):
		n_l.append(random.randint(minimum, maximum))
	# n3_l = n_l.copy()
	s = 0  # 用于存储未经处理随机数总和
	for i in n_l:
		s = i + s
	# print(s)
	n2_l = list()  # 用于存储处理后的随机数
	if b - s > 0:
		n_l.sort(reverse=True)
		# print(int((b-s)/a))
		aa = int((b - s) / a)
		for i2 in n_l:
			if i2 + int((b - s) / a) <= maximum:
				n2_l.append(i2 + int((b - s) / a))
			else:
				n2_l.append(maximum)
				n_l[-1] = n_l[-1] + int((b - s) / a) - (maximum - i2)
				n_l.sort(reverse=True)
		n_l.sort()
		if (b - s) % a != 0:
			for i4 in range(0, (b - s) % a):
				if n2_l[i4] == maximum:
					n_l.sort()
					n2_l[-1] = n2_l[-1] + 1
				else:
					n2_l[i4] = n2_l[i4] + 1
	else:
		n_l.sort()
		aa = int((s - b) / a)
		# print(int((s - b) / a))
		for i3 in n_l:
			if i3 - int((s - b) / a) >= minimum:
				n2_l.append(i3 - int((s - b) / a))
			else:
				n2_l.append(minimum)
				n_l[-1] = n_l[-1] - (int((s - b) / a) - (i3 - minimum))
				n_l.sort(reverse=False)
		bb = (s - b) % a
		if (s - b) % a != 0:
			n2_l.sort(reverse=True)
			for i4 in range(0, (s - b) % a):
				if n2_l[i4] == minimum:
					n2_l.sort(reverse=True)
					n2_l[0] = n2_l[0] - 1
				else:
					n2_l[i4] = n2_l[i4] - 1
	s2 = 0  # # 用于存储处理后的随机数总和，该值等于参数b
	for i3 in n2_l:
		s2 = i3 + s2
	# print(s2)
	n2_l.sort(reverse=True)
	return n2_l, s2, minimum


def excel_write(n, data, t, amount, name):
	rb = open_workbook(filename="./taxi/taxi_file/template.xls", formatting_info=True)

	wb: xlwt.Workbook
	ws0: xlwt.Worksheet
	wb = copy(rb)
	ws0 = wb.get_sheet(0)
	for i in range(n):
		ws0.write(i + 2, 0, data[i])
		ws0.write(i + 2, 1, t[i])
		ws0.write(i + 2, 3, amount[i])
		ws0.write(i + 2, 4, "上海")

	wb.save("./taxi/taxi_file/file/%s %d张.xls" % (name, n))


if __name__ == "__main__":
	logging.config.fileConfig("taxi/log/logging.conf")
	applogger = logging.getLogger("applog")
# ii = 0
# c = list()
# d = list()
# f = list()
# num1 = 4
# num2 = 377
# maximum1 = 100
# while ii < 10000:
# 	n = random_number(num1, num2, maximum1)
# 	applogger.debug(n)
# 	ii += 1
# 	c.append(n[1])
# 	d.append(n[0][-1])
# 	f.append(n[0][0])
# a1 = 0
# a2 = 0
# a3 = 0
# for iii, iiii, iiiii in zip(c, d, f):
# 	if iii != num2:
# 		a1 += 1  # 判断随机数的总和有没有不等于给定的总和的
# 	if iiii < n[2]:  # 判断随机数中是否有小于最小值的
# 		a2 += 1
# 	if iiiii > maximum1:  # 判断随机数中是否有大于最大值的
# 		a3 += 1
# print(a1, a2, a3)
