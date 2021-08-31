def sum_2_num(num1, num2):
    """两个变量的求和"""
    result = num1 + num2

    # return会直接返回，如果下面的还有代码是不执行的
    # 如果没有返回值，那么返回的结果为None
    return result
    # a = 10  # 这一行是不会被执行的


sum_result = sum_2_num(30, 40)
print("计算的结果为 %d" % sum_result)
