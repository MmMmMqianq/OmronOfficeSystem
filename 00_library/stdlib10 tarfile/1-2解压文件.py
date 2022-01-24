"""
解压缩操作步骤：
1. 打开已经存在的压缩文件；
	tarfile.open(name, mode, fileobj=None, bufsize=10240, **kwargs)
2. 解压缩文件；
	extract(name, path，pwd) 解压单个文件
	extractall(path, pwd) 解压所有文件
3. 关闭压缩文件；
"""
import tarfile

# 1. 打开已经存在的压缩文件
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
tp = tarfile.open("./test/tar01.tar.bz2", "r:bz2")  # 文件名的后缀和mode要对应起来

# 2. 解压缩文件
# extractall(path=None, members=None)
# path: 所有文件解压后保存的路径；
# pwd: 解压密码；

# extract(member, path=None)
# member: 要将哪个文件解压出来；
# path: 解压出来的文件存放到哪个文件夹下；
# pwd: 解压密码；
tp.extractall(path="./test/extract")  # 所有文件解压后保存的路径
tp.extract("./a/11.txt", "./test/extract1")  # 解压压缩文件 a 目录下的11.txt文件，和zipfile解压路径不要一样"a/11.txt"

# 3. 关闭压缩文件
# close()
tp.close()
