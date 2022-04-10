# Python 字典(Dictionary)
# 字典是另一种可变容器模型，且可存储任意类型对象。
#
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1: value1, key2: value2}

# 一个简单的字典实例：
tinydict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 也可如此创建字典：
tinydict1 = {'abc': 456}
tinydict2 = {'abc': 123, 98.6: 37}

# 访问字典里的值
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 8  # 更新
tinydict['School'] = "RUNOOB"  # 添加

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
#
# 显示删除一个字典用del命令，如下实例：

tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键是'Name'的条目
tinydict.clear()  # 清空字典所有条目
del tinydict  # 删除字典

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])
