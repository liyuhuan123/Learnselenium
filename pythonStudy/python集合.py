fruit = {"apple", "pear", "banana", "apple"}
# 去重功能
print(fruit)    # {'apple', 'banana', 'pear'}
# 快速判断元素是否在集合内
print('pear' in fruit)   # True
a = set("abcdefg")
b = set("acdsbh")
# 集合间的运算
# 1.a包含而b不包含的元素
print(a - b)   # {'f', 'g', 'e'}
# 2.b包含而a不包含的元素
print(b - a)   # {'h', 's'}
# 3.a和b的并集
print(a | b)    # {'c', 'g', 'h', 'f', 'd', 'e', 'b', 's', 'a'}
# 4.不同时包含于a和b的元素
print(a ^ b)    # {'g', 'h', 'f', 'e', 's'}
# 5.a和b的交集
print(a & b)    # {'c', 'd', 'a', 'b'}
# 集合的基本操作
# 1.添加元素
s = {1, 2, 3, 4}
# (1)添加集合中没有的
s.add(5)
print(s)   # {1, 2, 3, 4, 5}
# (2)添加集合中有的
s.add(1)
print(s)   # {1, 2, 3, 4, 5}
# (3)另一种添加元素的方法，参数可以是列表，元组，字典等
s1 = set(("Google", "fireFox", "edge"))
# 此时如果用此语句就会报错
# s1.add({1, 2, 3})
s1.update({1, 2, 3})
print(s1)   # {1, 'Google', 'edge', 2, 3, 'fireFox'}
s1.update([1, 2], [3, 4])
print(s1)   # {1, 2, 3, 4, 'Google', 'edge', 'fireFox'}
# 2.移除元素
# (1)使用remove()，将元素从s中移除，如果元素不存在，则会发生错误
s1.remove(1)
print(s1)   # {'fireFox', 2, 'Google', 3, 4, 'edge'}
# (2)使用discard()，如果元素不存在，不会发生错误
s1.discard(7)
s1.discard(2)
print(s1)   # {3, 4, 'Google', 'fireFox', 'edge'}
# (3)随即删除一个元素set()
# set集合的pop()方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
s1.pop()
print(s1)   # {3, 4, 'Google', 'edge'}
# 3.计算集合元素个数
print(len(s1))   # 4
# 4.清空集合
s1.clear()
print(s1)   # set()
# 5.判断元素是否在集合中存在
s1 = set(("Google", "fireFox", "edge"))
print("ie" in s1)   # False
print("fireFox" in s1)   # True
# 6.拷贝一个集合
s2 = s1.copy()
print(s2)   # {'fireFox', 'Google', 'edge'}
# 7.返回多个集合的差集
s1 = {1, 2, 3, 4, 5}
s2 = set((1, 3, 5, 7, 9))
print(s1.difference(s2))   # {2, 4}
# 8.移除集合中的元素，该元素在指定的集合也存在
s1.difference_update(s2)
print(s1)   # {2, 4}
print(s2)   # {1, 3, 5, 7, 9}
# 9.返回集合的交集
s1 = {1, 2, 3, 4, 5}
s2 = set((1, 3, 5, 7, 9))
print(s1.intersection(s2))   # {1, 3, 5}
print(s2)   # {1, 3, 5, 7, 9}
print(s1)   # {1, 2, 3, 4, 5}
s1.intersection_update(s2)
print(s1)   # {1, 3, 5}
print(s2)   # {1, 3, 5, 7, 9}
# 10.判断两个集合是否包含相同的元素，如果没有就返回True，否则返回False
s1 = {1, 2, 3, 4, 5}
s2 = set((1, 3, 5, 7, 9))
print(s1.isdisjoint(s2))   # False
# 11.判断指定集合是否为该方法参数集合的子集
print(s1.issubset(s2))   # False
s3 = {1, 2, 3}
print(s3.issubset(s1))   # True
# 12.判断该方法的参数集合是否为指定集合的子集
print(s1.issuperset(s3))   # True
# 13.返回两个集合中不重复的元素集合
print(s1.symmetric_difference(s2))   # {2,4,7,9}
# 14.移除当前集合在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
s1.symmetric_difference_update(s2)
print(s1)   # {2, 4, 7, 9}
print(s2)   # {1, 3, 5, 7, 9}
# 15.返回两个集合的并集
print(s1.union(s2))   # {1, 2, 3, 4, 5, 7, 9}
