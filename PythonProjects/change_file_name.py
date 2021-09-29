import os

# 目录路径
dir_path = "/Users/qianshaoqing/Desktop/宝宝照片/视频"

old_name_list = []
# 删除隐藏文件".DS_Store",只有MacOS会有这个隐藏文件
old_name_list_temp = os.listdir(dir_path)
for _name in old_name_list_temp:
	if not _name.startswith("."):
		old_name_list.append(_name)
print("删除前name_list: ", old_name_list)

# 构造新文件名
old_name_list_len = len(old_name_list)
new_name_list = [_ for _ in range(1, old_name_list_len + 1)]
for new_name_1 in new_name_list:
	new_name_list[new_name_list.index(new_name_1)] = "%d.mov" % new_name_1  # 注意要修改文件扩展名
print("删除前new_name_list: ", new_name_list)

# 删除旧文件名列表和新文件名列表中相同项，防止在重名时覆盖原文件
del_list = []
for new_name_2 in new_name_list:
	for old_name in old_name_list:
		if new_name_2 == old_name:
			del_list.append(old_name)
for del_name in del_list:
	old_name_list.remove(del_name)
	new_name_list.remove(del_name)
print("删除后name_list: ", old_name_list)
print("删除后new_name_list: ", new_name_list)

# 重命名
for name in old_name_list:
	path_old = dir_path + r"/" + name
	path_new = dir_path + r"/" + new_name_list[old_name_list.index(name)]
	os.rename(path_old, path_new)

all_files_num = old_name_list_len
files_changed_num = len(old_name_list)
print("%s 路径下的文件已被重命名，文件总数：%d，已更改文件数：%d" % (dir_path, all_files_num, files_changed_num))
