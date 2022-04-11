xiaoming_dict = {"name": "小明",
                 "gender": True,
                 "height": 1.75}
print(xiaoming_dict)

# 1. 取值
print(xiaoming_dict["name"])

# 2. 增加
xiaoming_dict["age"] = 18
print(xiaoming_dict)

# 3. 修改
xiaoming_dict["name"] = "xiaoming"
print(xiaoming_dict)

# 4， 删除
xiaoming_dict.pop("height")
print(xiaoming_dict)
