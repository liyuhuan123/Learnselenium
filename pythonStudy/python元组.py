# 创建元组
tup1 = ('Google', 'fireFox', 45, 78.9, [1, ])
tup2 = "a", "b", "c", 3, 4
# 创建空元组
tup3 = ()
# 创建一个元素的元组
tup4 = (4,)
print(tup1)    # ('Google', 'fireFox', 45, 78.9, [1])
print(tup2)    # ('a', 'b', 'c', 3, 4)
print(tup3)    # ()
print(tup4)    # (4,)
# 访问元组
tup1 = ('Google', 'fireFox', 45, 78.9, [1, ])
tup2 = (1, 2, 3, 4, 5, 6)
print(tup1[0])   # Google
print(tup2[1: 5])  # (2, 3, 4, 5)
# 修改元组
tup3 = tup1 + tup2
print(tup3)    # ('Google', 'fireFox', 45, 78.9, [1], 1, 2, 3, 4, 5, 6)
# 删除元组
tup1 = ('Google', 'fireFox', 45, 78.9, [1, ])
print(tup1)   # ('Google', 'fireFox', 45, 78.9, [1])
del tup1
# print(tup1) # 元组删除后，再打印会报错，同样也不能再对该元组进行其他任何操作
# 元组运算符
# 1.计算元素个数
print(len((1, 2, 3)))   # 3
# 2.连接
print((1, 2, 3) + (4, 5, 6))    # (1, 2, 3, 4, 5, 6)
# 3.复制
print((4,) * 4)    # (4, 4, 4, 4)
# 4.元素是否存在
print(3 in (1, 2, 3))   # True
# 5.迭代
for x in (1, 2, 3):
    print(x)
# 元组索引，截取
tup1 = (1, 2, 3, 4, 5)
print(tup1[1])  # 2
print(tup1[-2])  # 4
print(tup1[1:])   # (2, 3, 4, 5)
print(tup1[1: 4])  # (2, 3, 4)
# 元组内置函数
# 1.计算元组元素个数
tup1 = (1, 2, 3, 4, 5)
tup2 = ('Google', 'fireFox')
print(len(tup1))  # 5
# 2.返回元组中元素最大值
print(max(tup1))  # 5
print(max(tup2))   # fireFox
# 3.返回元组中元素最小值
print(min(tup1))   # 1
print(min(tup2))   # Google
# 4.将可迭代系列转换为元组
list1 = [1, 2, 3, 4, 5]
print(type(tuple(list1)))   # <class 'tuple'>
# 关于元组是不可变的
tup1 = (1, 2, 3, 4, 5)
print(id(tup1))    # 1888811609760
tup1 = ('Google', 'fireFox')
print(id(tup1))    # 1888811468944


