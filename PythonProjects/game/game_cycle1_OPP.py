#  -*- coding:utf-8 -*-
"""
游戏规则：n个人编号为1-n，围成一个圈，另一个人从第一个人位置开始走，每走三步对应圈上的人出去，最终剩下的是谁？
"""

numbers = input("总人数为：")
students = []
for member in range(1, int(numbers) + 1):
	students.append(member)
print(students)

position = 0

while len(students) > 1:
	count = 0
	for student in students:
		position += 1
		if position % 3 == 0:
			count += 1
			students[students.index(student)] = 0
	students.sort()
	students = students[count:int(numbers) + 1:]
	print(students)
	# if len(students) == 1.txt:
	# 	break
