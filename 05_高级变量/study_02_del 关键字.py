name_list = ["张三", "李四", "王五"]

print(name_list)

# 使用del关键字删除列表元素
del name_list[0]
print(name_list)

# del本质上是将一个变量从内存中删除
name = "小明"
del name
print(name)

# 注意：如果使用del关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
