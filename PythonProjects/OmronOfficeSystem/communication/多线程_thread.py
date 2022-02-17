import threading
import time
import logging
import logging.config


def fun1():
	global a
	for i in range(0, 5000):
		a += 1
		logging.debug("fun1完成"+str(a))
	logging.debug("11111111111111111111111完成" + str(a))


def fun2():
	global a
	for i in range(0, 5000):
		a += 1
		logging.debug("fun1完成" + str(a))
	logging.debug("22222222222222222222222完成" + str(a))


if __name__ == "__main__":
	logging.config.fileConfig("./log/logging.conf")
	logger = logging.getLogger("applog")
	a = 0
	t1 = threading.Thread(target=fun1)
	t1.start()
	t2 = threading.Thread(target=fun2)
	t2.start()

