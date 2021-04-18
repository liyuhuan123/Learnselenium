# 1.数据类型
import math
#
# a = 1.5
# print(int(a))  # 1
# a = 1
# print(float(a))  # 1.0
# print(complex(a))  # (1 + 0j)
# print(complex(a,1))  # (1 + 1j)
# 2.数学函数
# a = -1.9
# b = 2
# c = -3
# d = -1.9
# list = [-1.9, 2, -3, -1.9]
# print(abs(a))  # 1.9
# print(math.ceil(a))  # -1
# print((a > b) - (a < b))  # -1
# print((a > c) - (a < c))  # 1
# print((a > d) - (a < d))  # 0
# print(math.exp(1))    # 2.718281828459045
# print(math.fabs(a))   # 1.9
# print(math.floor(a))  # -2
# print(math.log(math.e))  # 1.0
# print(math.log(100, 10))  # 2.0
# print(math.log10(100))  # 2.0
# print(max(a, b, c, d))  # 2
# print(max(list))  # 2
# print(min(a, b, c, d))  # -3
# print(min(list))  # -3
# print(math.modf(a))  # (-0.8999999999999999, -1.0)
# print(math.pow(2, 3))  # 8.0
# print(round(a))  # -2
# print(math.sqrt(16))  # 4.0
# 随机数函数
# import random
#
# print(random.choice(range(100)))  # 66
# list = [-1.9, 2, -3, -1.9]
# random.shuffle(list)
# print(list)  # [2, -1.9, -3, -1.9]
# print(random.uniform(10, 20))  # 13.003644396627625

# str = "hello world!"
# print(str[0:6] + "lyh")  # hello lyh
# 字符串格式化
print("我叫%s今年%d岁！" % ('lyh', 21))  # 我叫lyh今年21岁！