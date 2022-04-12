students = [
    {"name": "小明"},
    {"name": "小美"}
]
# 在学生列表中搜索指定的姓名
find_name = "小白"
for stu_dict in students:
    if stu_dict["name"] == find_name:
        print("找到了 %s" % stu_dict)
        break
else:
    print("没有找到 %s" % find_name)
print("循环结束")
