import sys
list = [1, 2, 3, 4]
it = iter(list)   # 创建迭代器对象
print(next(it))   # 输出迭代器的下一个元素 1
print(next(it))   # 输出迭代器的下一个元素 2
print(next(it))   # 输出迭代器的下一个元素 3
print(next(it))   # 输出迭代器的下一个元素 4
# 在for循环中使用迭代器
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")
print()


