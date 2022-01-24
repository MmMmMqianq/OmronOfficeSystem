"""
tar是压缩模块的一种（使用tarfile模块）

tar有四种压缩方式，分别后缀如下：
	没有压缩 -> .tar
	gz压缩  -> .tar.gz
	bz2压缩 -> .tar.bz2
	xz压缩  -> .tar.xz

zip文件压缩步骤：（模块名zipfile）
1. 创建压缩文件，并打开；
	tar = tarfile.open(name, mode="r", fileobj=None, bufsize=10240, **kwargs)
2. 将文件添加到压缩文件中；
	zipfile.ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)
3. 关闭压缩文件；
	zipfile.ZipFile.close()
"""
import tarfile
import logging.config
import logging

logging.config.fileConfig("log/logging.conf")
applogger = logging.getLogger("applog")


# 1. 创建压缩文件，并打开；
# tarfile.open(name, mode, fileobj=None, bufsize=10240, **kwargs)
# name: 打开压缩文件的路径h和名字（需要加后缀，zipfile是不要加的）；
# mode: 设置操作模式（可以通过帮助文档查看）
# 		r     读取(以合适的方式读取)
# 		r:    不压缩
# 		r:bz2 bz2格式进行读取
# 		w     写入
# 		w:    不压缩写入
# 		w:bz2 bz2格式进行写入压缩
# 		x     异或
# 		x:bz2 bz2格式进行异或
# 		a     追加
# 		a:bz2 bz2格式进行追加压缩
tp = tarfile.open("./test/tar01.tar.bz2", "w:bz2")  # 文件名的后缀和mode要对应起来
applogger.debug(tp)

# 2. 将文件添加到压缩文件中；
# add(name, arcname, recursive=True, *, filter=None)
# name: 添加文件的路径；
# arcname: 添加到压缩文件中的路径和名称；
# recursive: 是否使用递归，如果是个文件夹是有用的；
# filter: 过滤器
tp.add("./test/1.txt", "./a/11.txt")
tp.add("./test/2.py", "22.py")
tp.add("./test/3", "33")

# 3. 关闭压缩文件；
# close()
tp.close()

