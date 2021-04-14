# 循环控制:continue
# continue:跳过后面的代码,立刻直接进入下一轮循环
for s in [1, 2, 3, 4, 5, 6]:
    if s == 3:
        continue   # 结束y这次循环,进入到t的循环
    print(s)