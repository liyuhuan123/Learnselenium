# 经典案例:while输出乘法口诀表
n = 1
while n <= 9:
    m = 1
    while m <= n:
        print(f'{n}*{m}={n*m}',end=' ')
        m += 1
    n += 1
    print()

