#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：game_cycle2_OPP.py
时间：2021/06/08
"""

cycle = [i for i in range(1, 501)]  # 列表推导式
step = 0

while len(cycle) > 1:
	dels = []
	for kid in cycle:
		step += 1
		if step % 3 == 0:
			dels.append(kid)

	for kid in dels:
		cycle.remove(kid)
	print(cycle)
