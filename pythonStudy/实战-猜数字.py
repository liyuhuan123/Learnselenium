# 在1-100之间随机产生一个整数,让用户反复猜,只提示'猜大了'或'猜小了'猜对结束游戏
# str---string    :     int----整数
# 键盘默认输入的是一个字符串类型的

import random
# m是1-100之间的一个整数
m = random.randint(1,100)
total = 5  # 可以猜的总数

count = 0  # 我猜了多少次了,默认是0次
# 只允许猜5次,如果5次没有猜对就结束游戏
while True:
    n = int(input('输入1-100之间的整数:'))
    if n < m:
        print('猜小了!')
    elif n > m:
        print('猜大了!')
    else:
        print('恭喜你,猜对了!')
        break
    count = count + 1
    if count >= total:
        print('很遗憾,游戏结束!')
        break
