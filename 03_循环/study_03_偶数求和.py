# 需求：计算0~100之间所有偶数累计求和和结果
i = 0
r = 0
while i <= 100:
    if i % 2 == 0:
        # print(i)
        r += i
    i += 1
print(r)
