# 创建字典
dict1 = {'name': 'lyh', 'sex': '女', 'age': 21}
# 访问字典里的值
print(dict1['name'])   # lyh
print(dict1['age'])    # 21
# 修改字典
dict1['age'] = 18
print(dict1['age'])   # 18
# 删除字典元素
del dict1['sex']
print(dict1)   # {'name': 'lyh', 'age': 18}
# 清空字典
dict1.clear()
print(dict1)    # {}
# 删除字典
del dict1
# 字典内置函数
dict1 = {'name': 'lyh', 'sex': '女', 'age': 21}
# 计算字典元素个数，即键的总数
print(len(dict1))   # 3
# 输出字典，以可打印的字符串表示
print(dict1)    # {'name': 'lyh', 'sex': '女', 'age': 21}
# 返回输入的变量类型，如果变量时字典就返回字典类型
print(type(dict1))   # <class 'dict'>
# 字典内置方法
# 1.删除字典内所有元素
dict1.clear()
print(dict1)   # {}
dict1 = {'name': 'lyh', 'sex': '女', 'age': 21}
# 2.返回一个字典的浅复制
dict2 = dict1.copy()
print(dict2)   # {'name': 'lyh', 'sex': '女', 'age': 21}
dict1['name'] = 'liyuhuan'
print(dict2)   # {'name': 'lyh', 'sex': '女', 'age': 21}
print(dict1)   # {'name': 'liyuhuan', 'sex': '女', 'age': 21}
# 3.返回指定值的键，如果键不存在返回default设置的默认值
print(dict1.get('age', 0))   # 21
print(dict1.get('class', 0))   # 0
# 4.如果键在字典dict里返回true，否则返回false
print('age' in dict1)   # True
# 5.以列表返回可比案例的（键，值）元组数组
print(dict1.items())   # dict_items([('name', 'liyuhuan'), ('sex', '女'), ('age', 21)])
# 6.返回一个迭代器，可以使用list()来转换为列表
print(dict1.keys())   # dict_keys(['name', 'sex', 'age'])
# 7.和get()类似，但如果键不存在字典中，将会添加键并将值设为default
dict1.setdefault('name', 'none')
print(dict1)   # {'name': 'liyuhuan', 'sex': '女', 'age': 21}
dict1.setdefault('class', 0)
print(dict1)   # {'name': 'liyuhuan', 'sex': '女', 'age': 21, 'class': 0}
# 8.把字典dict的键、值对更新到dict里
dict1.update(dict2)
print(dict1)   # {'name': 'lyh', 'sex': '女', 'age': 21, 'class': 0}
# 9.删除字典给定键key所对应的值，返回值为被删除的值，key值必须给出，否则，返回default值
print(dict1.pop('class', 1))   # 0
# 10.返回一个迭代器，可以使用list来转换为列表
print(list(dict1.values()))   # ['lyh', '女', 21]
# 11.随机返回并删除字典中的最后一堆键和值
print(dict1)  # {'name': 'lyh', 'sex': '女', 'age': 21}
print(dict1.popitem())   # ('age', 21)

