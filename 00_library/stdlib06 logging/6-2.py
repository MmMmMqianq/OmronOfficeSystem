"""
logging.basicConfig函数各参数:
    ·filename: 指定日志文件名，如my.log 或my.txt
    ·filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
    ·format: 指定输出的格式和内容，format可以输出很多有用信息，如下例所示:
    ·datefmt: 指定时间格式，同time.strftime()
    ·level: 设置日志级别，默认为logging.WARNING
    ·stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

logging模块常用format格式说明：
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名，python如：login.py
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号,在第几行打印的日志
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
    """
import logging


# 日志的格式化输出
logging.basicConfig(format="%(asctime)s|%(levelname)8s|%(filename)s|%(lineno)d|%(threadName)s|%(message)s",
                    datefmt="%%Y/%m/%d %H:%M:%S", level=logging.DEBUG)

name = "张三"
age = 18
logging.debug("姓名：%s，年龄：%d", name, age)