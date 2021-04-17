#  行与缩进
# if True:
#     print("True")
# else:
#     print("False")

# 多行语句:用反斜杠来连接
# item_one = 0
# item_two = 2
# item_three = 3
# total = item_one + \
#     item_two + \
#     item_three
# print(total)    # 5

# # 在[],{},()中的多行语句,不需要使用反斜杠(\)
# total = ['item_one', 'item_two', 'item_three']
# print(total)     # ['item_one', 'item_two', 'item_three']

# n = input()

# 单变量赋值
# a = 100  # 整型变量
# b = 100.0  # 浮点型变量
# c = 'abc'  # 字符串

# 多个变量赋值

# 以下实例，创建一个整型对象，值为1，从后向前赋值，三个变量被赋予相同的数值
# a = b = c = 1

# # 以下实例，两个整型对象1和2的分配给变量a和b，字符串对象‘abc’分配给变量c
# a, b, c = 1, 2, 'abc'
# print(a, b, c)  # 1 2 abc

# 查看变量所指的对象类型
# print(type(a))   # <class 'int'>
# print(type(b))   # <class 'int'>
# print(type(c))   # <class 'str'>
# print(isinstance(a, int))  # True

# 数值运算
# print(1 + 1)  # 加法 2
# print(1.1 - 1)  # 减法 0.10000000000000009
# print(2 * 3)   # 乘法 6
# print(2 / 4)  # 除法 0.5
# print(2 // 4)  # 除法：得到一个整数 0
# print(10 % 3)  # 取余 1
# print(2 ** 3)  # 乘方 8

# # String
# str = 'helloworld'
# print(str)  # 输出字符串 helloworld
# print(str[0: -1])  # 输出第一个到倒数第二个的所有字符 helloworl
# print(str[0])  # 输出字符串第一个字符 h
# print(str[2: 5])  # 输出从第三个字符到第五个的字符 llo
# print(str[2:])  # 输出从第三个开始的后的所有字符 lloworld
# print(str * 2)  # 输出字符串两次 helloworldhelloworld
# print(str + "test")  # 连接字符串helloworldtest
#
# print('hello\nworld')
# print(r'hello\nworld')

# list = ['abcd', 777, 3.2, 'rt', 90]
# list2 = [90]
# print(list)  # ['abcd', 777, 3.2, 'rt', 90]
# print(list[0])  # abcd
# print(list[1: 3])  # [777, 3.2]
# print(list * 2)  # ['abcd', 777, 3.2, 'rt', 90, 'abcd', 777, 3.2, 'rt', 90]
# print(list + list2)  # ['abcd', 777, 3.2, 'rt', 90, 90]

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)

# 元组
tuple = ('abcd', 777, 3.2, 'rt', 90)
tuple2 = (90, 2)
print(tuple)  # ('abcd', 777, 3.2, 'rt', 90)
print(tuple[0])  # abcd
print(tuple[1: 3])  # (777, 3.2)
print(tuple * 2)  # ('abcd', 777, 3.2, 'rt', 90, 'abcd', 777, 3.2, 'rt', 90)
print(tuple + tuple2)  # ('abcd', 777, 3.2, 'rt', 90, 90)

# Set
# 第一种创建方法
arr = {12, 12, 34, 'ab', 'ab', 'ac'}
print(arr)  # 输出集合,重复的元素被自动去掉 {34, 12, 'ac', 'ab'}
# 第二种创建方法
a = set('11222345')
b = set('245777')
# set的集合运算
print(a)  # {'2', '3', '5', '1', '4'}
print(b)  # {'7', '4', '5', '2'}
print(a - b)  # a和b的差集 {'3', '1'}
print(a | b)  # a和b的并集 {'7', '4', '1', '5', '2', '3'}
print(a & b)  # a和b的交集 {'4', '5', '2'}
print(a ^ b)  # a和b中不同时存在的元素 {'7', '1', '3'}

# 字典
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

dict = {}
dict['one'] = "lyh"
dict[2] = "liyuhuan"

tinydict = {'name': 'liyuhuan', 'sex':'女', 'age': 21}

print(dict['one'])       # 输出键为 'one' 的值  lyh
print(dict[2])           # 输出键为 2 的值   liyuhuan
print(tinydict)          # 输出完整的字典   {'name': 'liyuhuan', 'sex': '女', 'age': 21}
print(tinydict.keys())   # 输出所有键   dict_keys(['name', 'sex', 'age'])
print(tinydict.values())  # 输出所有值   dict_values(['liyuhuan', '女', 21])
