# input函数
name = input("姓名：")
print(name)

# 买苹果增强
# 收银员输入苹果的价格，单位：元/斤
# 收银员输入用户购买苹果的重量，单位：斤
# 计算并且输出付款金额
price_str = input("请输入苹果单价：")
weight_str = input("请输入苹果重量：")

# 计算金额，字符串转为小数
price = float(price_str)
weight = float(weight_str)

# 计算
money = price * weight
print(money)
