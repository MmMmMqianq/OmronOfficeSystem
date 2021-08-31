def mutiple_table():
    row = 1
    while row <= 9:

        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, row * col), end="\t")  # 此处用了一个制表符使每行数据垂直对齐
            col += 1

        print("")
        row += 1
