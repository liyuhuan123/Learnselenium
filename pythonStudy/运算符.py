# 1.算术运算符
a = 21
b = 10
print(a + b)   # 31
print(a - b)   # 11
print(a * b)   # 210
print(a / b)   # 2.1
print(a % b)   # 1
print(a ** b)  # 16679880978201
print(a // b)  # 2
# 2.比较运算符
a = 21
b = 10
c = 21
d = 10
print(a == b)   # False
print(a == c)   # True
print(a != b)   # True
print(a != c)   # False
print(a >= b)   # True
print(a <= b)   # False
# 3.赋值运算符
a = 21
b = 10
# 4.位运算符
a = 60
b = 13
print(a & b)   # 12
print(a | b)   # 61
print(a ^ b)   # 49
print(~a)      # -61
print(a << 2)  # 240
print(a >> 2)  # 15
# 5.逻辑运算符
a = 10
b = 20
if a and b:
    print("变量a和b都为true")  # 变量a和b都为true
else:
    print("变量a和b有一个不为true")
if a or b:
    print("变量a和b都为true，或其中一个变量为true")  # 变量a和b都为true，或其中一个变量为true
else:
    print("变量a和b都不为true")
a = 0
if a and b:
    print("变量a和b都为true")
else:
    print("变量a和b有一个不为true")  # 变量a和b有一个不为true
if a or b:
    print("变量a和b都为true，或其中一个变量为true")  # 变量a和b都为true，或其中一个变量为true
else:
    print("变量a和b都不为true")
if not a:
    print("a为False")  # a为False
# 6.成员运算符
a = 10
b = 20
c = 1
list = [1, 2, 3, 4, 5]
print(a in list)   # False
print(c in list)   # True
print(a not in list)  # True
# 7.身份运算符
a = 20
b = 20
print(a is b)  # True
print(a is not b)  # False
b = 30
print(a is b)  # False
print(a is not b)  # True
# is和==区别
a = [1,2,3]
b = a
print(b == a)  # True
print(b is a)  # True
b = a[:]
print(b == a)  # True
print(b is a)  # False