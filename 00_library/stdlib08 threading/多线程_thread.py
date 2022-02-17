import threading
import time
import logging
import logging.config


def fun1(a, b):
	logging.debug(threading.current_thread())  # 返回当前正在执行的线程
	time.sleep(5)
	logging.debug("fun1完成"+str(a+b))


def fun2(aa, bb):
	logger.debug(threading.main_thread())
	time.sleep(5)
	logger.debug("fun2完成"+str(aa+bb))


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	for i in range(3):
		t1 = threading.Thread(target=fun1, args=(1, 2,))
		t1.start()
	time.sleep(3)
	t2 = threading.Thread(target=fun2, args=(3, 4,))
	logger.debug(threading.active_count())  # 返回总的线程数
	logger.debug(threading.enumerate())  # 返回当前正在执行的所有线程组成的列表
	logger.debug(threading.current_thread())  # 返回当前正在执行的线程
