# 定义一个函数能够打印5行的分割线

def print_line(char, times):
    print(char * times)


def print_lines(rows, char, times):
    """
    打印自定行数的分隔符
    :param rows: 行数
    :param char: 字符
    :param times: 次数
    """
    row = 0
    while row < rows:
        print_line(char, times)
        row += 1


print_lines(5, "*", 50)
