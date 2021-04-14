# 为什么使用函数
# 2个目的
# 1.降低编程难度
# 2.增加代码复用

# 1+2+3+.....+100
# 不使用函数
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print(sum)


# 定义一个求和函数
def qiu_he(n, m):
    sum = 0
    while n <= m:
        sum += n
        n += 1
    return sum

# 调用函数
print(qiu_he(1,100))

