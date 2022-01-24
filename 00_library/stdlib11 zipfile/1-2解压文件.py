"""
解压缩操作步骤：
1. 打开已经存在的压缩文件；
2. 解压缩文件；
3. 关闭压缩文件；
"""
# 1. 打开已经存在的压缩文件；
import zipfile

# 1. 打开已经存在的压缩文件；
zp = zipfile.ZipFile("./test1/zip01.zip", "r")  # 要用读取方式

# 2. 解压缩文件；
# zipfile.ZipFile.extractall(path=None, members=None, pwd=None)
# path: 所有文件解压后保存的路径；
# pwd: 解压密码；

# zipfile.ZipFile.extract(member, path=None, pwd=None)
# member: 要将哪个文件解压出来；
# path: 解压出来的文件存放到哪个文件夹下；
# pwd: 解压密码；
zp.extractall(path="./test1/extract", pwd=None)  # 所有文件解压后保存的路径
zp.extract("a/11.txt", "./test1/extract2", pwd=None)  # 解压压缩文件 a 目录下的11.txt文件，和tarfile解压写法不一样 "./a/11.txt"

# 3， 关闭压缩文件；
zp.close()
