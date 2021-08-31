gl_num_list = [1, 2, 3]
gl_num = 10


def demo(num, num_list):

    # num += num 相当于num = num + num, 执行了赋值语句，所以不会改变全局变量gl_num的值
    num += num
    print("函数中执行num += num结果为{}".format(num))

    # num_list += num_list 相当于 num_list.extend(num_list)，执行了extend方法，所以会改变全局变量gl_num_list的值
    num_list += num_list
    print("函数中执行num_list += num_list结果为{}".format(num_list))


demo(gl_num,gl_num_list)
