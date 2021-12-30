import threading
import time
import logging
import logging.config


def fun1(i):
	logging.debug(threading.current_thread())  # 返回当前正在执行的线程
	time.sleep(i+i)
	logging.debug("fun1完成")


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	t_pool = list()
	for i in range(3, 6):
		t1 = threading.Thread(target=fun1, args=(i,))
		t_pool.append(t1)

	for sub in t_pool:
		sub.start()

	# for sub_j in t_pool:
	# 	sub_j.join()  # 左右子线程结束后执行主线程

	# t_pool[0].join(7)  # 每个子线程都执行完之后主线程才往下执行，join(timeout)还可以设置超时时间，改时间为从执行join开始计算时间
	# logger.debug(t_pool[0].is_alive())
	#
	# t_pool[1].join(1)
	# logger.debug(t_pool[1].is_alive())
	#
	# t_pool[2].join(3)
	# logger.debug(t_pool[2].is_alive())

	logger.debug("------主进程结束------")