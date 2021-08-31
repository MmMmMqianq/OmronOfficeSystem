def sum_num(num):

    print(num)
    if num == 1:  # 递归函数必须要有出口，否则会出现死循环
        return
    sum_num(num-1)


sum_num(10)

# 例子：数值累加计算
def sum_numbers(num):
    # 1. 出口
    if num == 1:
        return 1

    # 2. 数字的累加 num + (1+2+3...+(num-1))
    # 假设 sum_numbers 能够正确处理 1+2+3...+(num-1)
    temp = sum_numbers(num - 1)
    return num + temp


print(sum_numbers(100))

