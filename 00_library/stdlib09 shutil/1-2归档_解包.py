"""
归档和解包操作：
归档：将一个文件夹中的内容转换成一个压缩文件，总的大小是不变的；方便转移。
解包：将归档的文件进行和释放；

压缩：将多个文件先进行归档，再使用或者不使用算法压缩，添加到一个压缩文件中，总的大小变小；
解压：压缩的反向操作，将文件释放出来

注意：压缩属于归档
"""
import logging.config
import logging
import shutil

logging.config.fileConfig("log/logging.conf")
applogger = logging.getLogger("applog")

# 归档操作：
# shutil.make_archive(base_name, format，root_dir)
# base_name: 归档后文件的保存路径和名称（没有文件后缀部分，后缀通过format设置）
# format: 设置归档文件的后缀（通产为 zip和tar'）
# root_dir: 设置需要归档的文件夹根目录
# return: 返回归档后文件的路径
result = shutil.make_archive("./test5/gd", "zip", "./test4")
applogger.debug(result)

# 解包操作
# shutil.unpack_archive(filename, extract_dir, format=None)
# filename: 归档文件的完整路径
# extract_dir: 归档文件解包的目标文件夹名称，如果没有写默认为当前的工作目录
# return: None
shutil.unpack_archive("./test5/gd.zip", "./test5")


# 查看归档支持的格式
# 返回：[(文件格式名称，该格式的介绍)]
result1 = shutil.get_archive_formats()
applogger.debug(result1)

# 查看解包支持的格式
# 返回 [(文件格式名称，对应格式的后缀，该格式的说明信息)]
result2 = shutil.get_unpack_formats()
applogger.debug(result2)

# 注册自定义的压缩格式
# shutil.register_archive_format()
