i = 0
while i <= 10:
    if 3 <= i <= 6:
        # 注意：在循环中，如果使用continue这个关键字
        # 在使用关键字之前，需要先确认循环计数是否修改，否则可能导致死循环
        i += 1
        continue  # continue 某一条件满足时，不执行后续代码，跳转到while的判断语句
    print(i)
    i += 1
