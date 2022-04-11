name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list)

# 1. 取值和取索引
print(name_list[2])
print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"
print(name_list)

# 3. 增加
name_list.append("zhaoliu")
print(name_list)
name_list.insert(1, "Tom")
print(name_list)

temp_list = ["孙悟空", "猪悟能", "沙悟净"]
name_list.extend(temp_list)
print(name_list)

# 4. 删除
name_list.remove("wangwu")
print(name_list)
name_list.pop()
print(name_list)
name_list.pop(3)
print(name_list)

name_list.clear()
print(name_list)
