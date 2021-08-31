for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    print('会执行吗')  # 如果for循环中有break退出循环，那么else下的语句就不会被执行，
                      # 否则在for循环结束后执行else下的语句
