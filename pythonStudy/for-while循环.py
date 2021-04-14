# 经典案例:while+for输出乘法口诀表
n = 1
while(n <= 9):
    for m in range(1,n + 1):
        print(f'{n}*{m}={n*m}',end=' ')
    n = n + 1
    print()