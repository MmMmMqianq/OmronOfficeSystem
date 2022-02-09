import logging.config
import logging
import shutil

logging.config.fileConfig("log/logging.conf")
applogger = logging.getLogger("applog")

# copy() 复制文件，变更文件的属性，返回复制后的文件路径。如果有相同名字的文件会被覆盖。
result1 = shutil.copy("./test1/file.txt", "./test2/file_copy.txt")
applogger.debug(result1)

# copy2() 复制文件，保留原有的属性，返回复制后的文件路径。如果有相同名字的文件会被覆盖。
result2 = shutil.copy2("./test1/file.txt", "./test2/file_copy2.txt")
applogger.debug(result2)

# copyfileobj() 复制文件内容到另外一个文档内，无返回值，一般在文件后面追加复制的内容可用。两个文件的类型不一定要一样的
# shutil.copyfileobj(open("src", "r"), open("dst", "w"))
shutil.copyfileobj(open("./1-1.py", "r"), open("./test2/1-1_copyfileobj.txt", "w"))

# copyfile() 复制文件内容到另外一个文档内，返回复制后的文件路径。
result3 = shutil.copyfile("./1-1.py", "./test2/1-1_copyfile.txt")
applogger.debug(result3)

# # copytree() 复制文件夹
# result4 = shutil.copytree("./test2", "./test2_copy")  # 如果目录已经存在则会报FileExistsError错误
# applogger.debug(result4)

# rmtree() 删除目录，无返回值。删除是不经过回收站的。
# shutil.rmtree("./test2_copy")  # 如果文件夹不存在报FileNotFoundError错误

# move() 移动文件或者目录，返回移动后的路径
# result5 = shutil.move("./test2/file_copy2.txt", "./test3") # 如果文件或者文件夹已经存在会报错

# which() 获取系统命令的路径
result6 = shutil.which("pip")
applogger.debug(result6)

# disk_usage() 获取磁盘使用信息
result7 = shutil.disk_usage("./test2")
applogger.debug(result7)