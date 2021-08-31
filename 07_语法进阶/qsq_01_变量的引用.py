def test(num):  # num为形参
    print(num, id(num))

    # >1. 定义一个字符串变量
    result = "Hello Python"
    print("result 变量保存的字符串{0}内存地址是：{1}".format(result, id(result)))

    # >2. 将字符串变脸返回
    return  result

a = 10  # a为实参，a保存的是数据10的引用（绝对地址）
print("{0}的绝对值为{1}".format(a, id(a)))

# 调用test函数，本质上传递的是实参保存数据的引用（绝对地址）
#而不是实参保存的数据
b = test(a)
print(id(b))  # id(b)的值和id(result)的值是一样的，说明函数返回值传递的也是引用
