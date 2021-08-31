student = [
    {'name':'阿土'},
    {'name':'小美'}
]

find_name = "阿土"

for dict_name in student:
    print(dict_name)
    if dict_name['name'] == find_name:
        print('找到 %s 了' % find_name)
        break
else:
    print('没有找到 %s')