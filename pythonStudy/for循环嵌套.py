# python的for循环嵌套(for里面还有for)
# 经典案例:输出乘法口诀表
for i in range(1,10):
    for j in range(1,i + 1):
        # end=' '指定以空格结束
        print(f'{i} * {j} = {i * j}',end='  ')
    # 换行
    print()
