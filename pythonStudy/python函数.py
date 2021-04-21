def hello():
    print("hello world!")
hello()

def hello2(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "一样大"
x = 1
y = 2
print(max(x, y))
# 参数传递
