n = 100
sum = 0
while n > 0:
    sum += n
    n -= 1
print(sum)   # 5050
# while循环中使用else语句
x = 1
while x > 1:
    print("x > 1")
else:
    print("x = 1")
# for循环
list = ["c", "java", "python", "php"]
for x in list:
    print(x, end=" ")
print()
# for循环中的else语句
for x in list:
    if x == "python":
        print("python")
        break
    else:
        print(1)
else:
    print("循环结束")
print("退出")
# range()函数
for i in range(10):
    print(i, end=" ")
print()
for i in range(5, 10):
    print(i, end=" ")
print()
for i in range(5, 10, 2):
    print(i, end=" ")
print()
a = (1, 2, 3, 4, 5)
for x in range(len(a)):
    print(a[x], end=" ")
print()
# pass语句
for x in "fireFox":
    if x == 'o':
        pass
        print("执行pass语句")
    print("当前字母：", x)
print("结束循环")