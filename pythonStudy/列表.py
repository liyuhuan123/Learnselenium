# 列表[]
my_list = [1, 2, 'a', 1.3]
print(my_list[2])   # a

# 列表增加元素(末尾增加):append()
my_list.append(111)
print(my_list)      # [1, 2, 'a', 1.3, 111]

# 插入元素(指定位置插入):insert()
my_list.insert(1, 'python')
print(my_list)      # [1, 'python', 2, 'a', 1.3, 111]

# 扩充列表:extend(),必须接一个序列
# my_list.extend(1)
# print(my_list)     # 报错:原因是整型是不可迭代的

my_list.extend('s')
print(my_list)       # [1, 'python', 2, 'a', 1.3, 111, 's']

my_list.extend('python')
print(my_list)       # [1, 'python', 2, 'a', 1.3, 111, 's', 'p', 'y', 't', 'h', 'o', 'n']

my_list.extend([22, 33, 44])
print(my_list)       # [1, 'python', 2, 'a', 1.3, 111, 's', 'p', 'y', 't', 'h', 'o', 'n', 22, 33, 44]

# 列表删除元素:pop():从尾部删除元素
my_list2 = [1, 2, 'a', 1.3]
my_list2.pop()
print(my_list2)     # [1, 2, 'a']

# 列表删除元素:remove():指定元素删除
my_list2.remove(1)
print(my_list2)     # [2, 'a']

# 列表的修改
my_list3 = [1, 2, 'a', 1.3]
my_list3[2] = 33
print(my_list3)    # [1, 2, 33, 1.3]
