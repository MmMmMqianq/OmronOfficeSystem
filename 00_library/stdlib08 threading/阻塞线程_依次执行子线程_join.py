import threading
import time
import logging
import logging.config


def fun1(a, b):
	logging.debug(threading.current_thread())  # 返回当前正在执行的线程
	time.sleep(5)
	logging.debug("fun1完成"+str(a+b))


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	for i in range(3):
		t1 = threading.Thread(target=fun1, args=(1, 2,))
		t1.start()
		t1.join()  # 每给线程被启动后就会被阻塞，直到该线程执行完主线程才往下走
	logger.debug("------主进程结束------")