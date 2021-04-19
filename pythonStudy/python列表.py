# 更新列表
list = ['喜茶', '一點點', '星巴克', 19, 89.9]
list[2] = 78
print(list)    # ['喜茶', '一點點', 78, 19, 89.9]
# 添加元素
list.append('书亦烧仙草')
print(list)    # ['喜茶', '一點點', 78, 19, 89.9, '书亦烧仙草']
list1 = [67, 90]
# 添加列表
list.append(list1)
print(list)   # ['喜茶', '一點點', 78, 19, 89.9, '书亦烧仙草', [67, 90]]
# 删除列表元素
del list[len(list) - 1]
print(list)   # ['喜茶', '一點點', 78, 19, 89.9, '书亦烧仙草']
# python列表脚本操作符
print(len([1, 2, 3]))   # 3
print([1, 2, 3]+[4, 5, 6])   # [1, 2, 3, 4, 5, 6]
print([1] * 4)   # [1, 1, 1, 1]
print(3 in [1, 2, 3])   # True
# 迭代，输出结果：  1,2,3,
for x in [1, 2, 3]:
    print(x, end=',')
print()
# python列表截取与拼接
list = [1, 2, 3, 34]
print(list[1])   # 2
print(list[-2])  # -2
print(list[1:])   # [2,3,24]
# 嵌套列表
list = [[1, 2, 3], 9, [2, ]]
print(list)   # [[1, 2, 3], 9, [2]]
print(list[0][1])   # 2
# python列表函数
list = [1, 2, 3, 9, 2]
print(len(list))   # 5
print(max(list))   # 9
print(min(list))   # 1
# python列表方法
list.append(10)
print(list)   # [1, 2, 3, 9, 2, 10]
print(list.count(2))  # 2
print(list.index(2))   # 1
list.insert(1, 7)
print(list)   # [1, 7, 2, 3, 9, 2, 10]
print(list.pop())   # 10
list.remove(2)
print(list)   # [1, 7, 3, 9, 2]
list.reverse()
print(list)    # [2, 9, 3, 7, 1]
list.sort()
print(list)   # [1, 2, 3, 7, 9]
list1 = list.copy()
print(list1)   # [1, 2, 3, 7, 9]



