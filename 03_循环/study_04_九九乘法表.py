# 利用循环嵌套打印九九乘法表
# row = 0
# while row < 5:
#     j = row + 1
#     print(j * "*")
#     row += 1

row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    print("")
    row += 1
