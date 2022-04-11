# 1. 定义一个print_line函数打印一组*组成的分割线

# def print_line():
#     print("*" * 50)


# 2. 定一个一个函数打印特殊字符组成的分割线
# def print_line(char):
#     print(char * 50)

# 3. 定义一个函数打印任意重复次数的分割线
def print_line(char, times):
    print(char * times)


print_line("=", 20)
