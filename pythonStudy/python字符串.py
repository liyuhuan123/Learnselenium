# 字符串操作
a = "hello"
b = "world"
print(a + b)   # helloworld
print(a * 2)   # hellohello
print(a[1])    # a
print(a[1 : 4])   # ell
print('h' in a)   #True
print('m' in b)   # False
print(r'hello\nworld')   # hello\nworld
# 字符串格式化
print("我叫%s，今年%d岁" % ('lyh', 21))   # 我叫lyh，今年21岁
# python三引号
str = """ 这是一个多行字符串的实例
多行字符串可以使用制表符
TAB(\t)
也可以使用换行符[\n]
"""
print(str)

# f-string
name = 'world'
res = f'hello {name}'
print(res)   # hello world
print(f'{1 + 2}')   # 3
dic = {'name': 'lyh', 'sex': '女', 'age': 21}
print(f'{dic["name"]},{dic["sex"]}')   # lyh,女
x = 1
print(f'{x + 2}')
# python字符串内建函数
str = "hello world!"
# 将首字母转为大写
print(str.capitalize())   # Hello world!
# 中心位置扩充字符串
print(str.center(20, '#'))  # ####hello world!####
# 统计字符串内特定子字符串出现的次数，可以设置特定长度
print(str.count('l', 0, 7))   # 2
print(str.count('l'))    # 3
str2 = "hello   world!"
# 将tab键转为空格
print(str.expandtabs())    # hello world!
# 判断是否以特定字符串结尾，可以设置特定长度
print(str.endswith('!'))   # True
print(str.endswith('o', 0, 3))   # False
# 判断特定字符是否在字符串中出现过，返回出现位置的下标
print(str.find('m', 0, len(str)))    # -1
print(str.find('h'))    # 0
# 判断特定字符是否在字符串中出现过，返回出现位置的下标
# print(str.index('m', 0, len(str)))   # 不存在就抛异常
print(str.index('o'))     # 4
str3 = "我爱编程"
print(str.isalnum())   # False
print(str3.isalnum())  # True
print(str3.isalpha())  # True
print(str.isalpha())   # False
str4 = '9297387'
print(str.isdigit())   # False
print(str4.isdigit())  # True
print(str.islower())   # True
print(str.isnumeric())  # False
print(str4.isnumeric())   # True
str5 = "    "
print(str5.isspace())   # True
str6 = "HELLOWORLD"
print(str6.isupper())   # True
print(str.isupper())    # False
list = ['h','e','l','l','o']
print(str.join(list))  # hhello world!ehello world!lhello world!lhello world!o
print(len(str))   # 12
print(str.ljust(20), '#')   # hello world!        #
print(str6.lower())    # helloworld
str7 = '    hello world   '
print(str7.lstrip())   # hello world
print(max(str6))    # W
print(min(str6))   # D
print(str7.replace(' ', '#', 4))   # ####hello world
print(str7.rfind('d', 0, len(str7)))   # 14
print(str7.rfind(' '))  # 17
print(str.rindex('d', 0, len(str)))  # 10
print(str.rindex('d'))    # 10
print(str.rjust(20, '#'))   # ########hello world!
print(str7.rstrip())   #     hello world
print(str7.split(" ", 2))     # ['', '', '  hello world   ']
print(str7.split(" "))    # ['', '', '', '', 'hello', 'world', '', '', '']
print(str.startswith('h', 0, len(str)))  # True
print(str.startswith('h'))   # True
print(str7.strip())    # hello world
str8 = "HelloWorld"
print(str8.swapcase())   # hELLOwORLD
print(str8.upper())   # HELLOWORLD
print(str.zfill(20))   # 00000000hello world!
print(str4.isdecimal())   # True



