"""
logging的高级应用：

logging模块采用了模块化设计，主要包括四种组件：
Loggers: 记录器，提供应用程序代码能直接使用的接口；
Handlers: 处理器，将记录器产生的日志发送至目的地；
Filters: 过滤器，提供更好的粒度控制，决定哪些日志会被输出，日志的输出级别就是一种过滤器；
Formatters: 格式化器，设置日志内容的组成结构和消息字段；
"""
import logging

# 以编程的方式实现日志的输出（不推荐）

# 1. 创建一个记录器logger，记录器名字设置为appLogger，不设置默认为root
logger = logging.getLogger("abc.appLogger")
logger.setLevel(logging.DEBUG)  # 如果处理器的等级比记录器底则以记录器等级输出

# 2. 创建处理器Handler
# 创建一个控制台输出的处理器
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# 创建一个文件输出的处理器
fileHandler = logging.FileHandler(filename="demo1.log", mode="w")
fileHandler.setLevel(logging.INFO)

# 3. 创建一个格式化器
formatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s|%(lineno)d|%(threadName)s|%(message)s",
                              datefmt="%Y/%m/%d %H:%M:%S")

# 4. 创建一个过滤器
flt = logging.Filter("abc")  # 只要记录器的名字是以"abc."就能正常输出

# 5. 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 6. 给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 7. 给记录器和处理器加上过滤器
logger.addFilter(flt)
# fileHandler.addFilter(flt)


# 8. 输出日志
logger.debug("This is debug log")
logger.info("This is info log")
logger.warning("This is warning log")
logger.error("This is error log")
logger.critical("This is critical log")
