"""
归档和解包操作：
归档：将一个文件夹中的内容转换成一个压缩文件，总的大小是不变的；方便转移。
解包：将归档的文件进行和释放；

压缩：将多个文件先进行归档，再使用或者不使用算法压缩，添加到一个压缩文件中，总的大小变小；
解压：压缩的反向操作，将文件释放出来
注意：压缩属于归档

文件压缩的作用：
1.下载一个文件需要解压缩；
2.发送邮件，压缩之后发送；
3.在线打包，方便下载

zip文件压缩步骤：（模块名zipfile）
1. 创建压缩文件，并打开；
	zipfile.ZipFile(file, mode="r", compression=0, allowZip64=True, compresslevel=None)
2. 将文件添加到压缩文件中；
	zipfile.ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)
3. 关闭压缩文件；
	zipfile.ZipFile.close()

注意事项：
1. 如果想把一个文件夹中的内容都压缩了需要使用递归操作或者使用shutil模块归档；
2. 密码：目前Python 3.10版本还没有解决密码问题，设置和没有设置一个效果；
"""

import zipfile
import logging.config
import logging

logging.config.fileConfig("log/logging.conf")
applogger = logging.getLogger("applog")

# 1. 创建压缩文件，并打开；
# zp = zipfile.ZipFile(file, mode="r", compression=0, allowZip64=True, compresslevel=None)
# file: 压缩文件的路径；
# mode: 设置操作文件的模式（和文件操作模式是一样的）；
# compression: 设置是否使用压缩还是保持原文件大小；ZIP_STORED = 0，ZIP_DEFLATED = 8，ZIP_BZIP2 = 12，ZIP_LZMA = 14
# allowZip64: 设置压缩文件是否超过2G大小，True为超过2G；
# compresslevel: 设置压缩等级；
# return: 返回压缩文件指针
zp = zipfile.ZipFile(file="./test1/zip01.zip", mode="w")  # 路径必须要是已经存在的
applogger.debug(zp)

# 2. 将文件添加到压缩文件中；
# zipfile.ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)
# filename: 需要添加的文件；
# arcname: 在压缩文件中的路径和名称；
zp.write("./test1/1.txt", "./a/11.txt")
zp.write("./test1/2.py", "22.py")
zp.write("./test1/3", "33")

# 3. 关闭压缩文件；
# zipfile.ZipFile.close()
zp.close()
