gl_num = (1, 2, 3, 4)
gl_dict = {"name": "小明", "age": 18}


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(gl_num, gl_dict)  # 这个是没拆包的语法，会将gl_num, gl_dict两个变量作为一个元组出进去，字典是空值
demo(*gl_num, **gl_dict)  # 这个语法为拆包语法，回见gl_num传给元组，gl_list传给字典

