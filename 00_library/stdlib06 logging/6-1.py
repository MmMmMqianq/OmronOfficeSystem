"""
logging.basicConfig函数各参数:
	·filename: 指定日志文件名，如my.log 或my.txt
	·filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
	·format: 指定输出的格式和内容，format可以输出很多有用信息，如下例所示:
	·datefmt: 指定时间格式，同time.strftime()
	·level: 设置日志级别，默认为logging.WARNING
	·stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
"""
import logging


# 默认的日志输出级别为warning，可以通过logging.baseConfig()
logging.basicConfig(filename="demo.log",filemode="w", level=logging.DEBUG)  # 设置日志数输出级别，将日志输出到指定的文件里,"w"为先清空再写入

# logging是多线程的，并发的
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")

