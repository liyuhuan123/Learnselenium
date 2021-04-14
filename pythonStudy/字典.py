# 字典{}
# 键值对 键-->值
user = {
    'name': 'Tom',
    'age': 18,
    'sex': 'male'
}
print(user)    # {'name': 'Tom', 'age': 18, 'sex': 'male'}
print(user['age'])  # 18

user['age'] = 28
print(user)  # {'name': 'Tom', 'age': 28, 'sex': 'male'}

# 可以通过赋值的方式给字典里面添加元素
user['fav'] = '打篮球'
print(user)   # {'name': 'Tom', 'age': 28, 'sex': 'male', 'fav': '打篮球'}
