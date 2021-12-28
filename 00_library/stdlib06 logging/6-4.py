import logging


import logging
import logging.config

# 以配置文件方式实现日志的输出（推荐）
logging.config.fileConfig("logging.conf")  # 加载配置文件

rootlogger = logging.getLogger()
rootlogger.debug("This is debug log,root.")

applogger = logging.getLogger("applog")
applogger.debug("This is debug log,applog")

a = "abc"
try:
	int(a)
except Exception as e:
	applogger.error(e)  # 这种方式只能打印报错的内容，不会打印栈信息（具体到哪行出的错）
	applogger.exception(e)  # 既打印报错内容又会打印栈信息
