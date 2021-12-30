"""
daemon=True时，主线程不守护子线程，主线程结束子线程自动结束；
daemon=False时，主线程守护子线程，主线程等待子线程执行完成；

如果有两个子线程，分别设置了True和False，那么主线程守护设置为False的子线程。
"""
import threading
import time
import logging
import logging.config


def fun(a):
	time.sleep(a)


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	t1 = threading.Thread(target=fun, args=(8,), daemon=True)
	t1.start()

	t2 = threading.Thread(target=fun, args=(3,), daemon=False)
	t2.start()

	logger.debug("——————主线程最后一行代码——————")