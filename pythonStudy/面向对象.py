class MyClass:
    i = 132
    def fun(self):
        return 'hello world!'

    def __init__(self):
        self.data = []
# 实例化类
x = MyClass()
print(x.i)  # 132
print(x.fun())  # hello world!

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)    # 3.0 -4.5

class Test:
    def prt(Baidu):
        print(Baidu)
        print(Baidu.__class__)
t = Test()
t.prt()     # <class '__main__.Test'>

class People:
    name = ''
    age = 0
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
            print("%s说：我%d岁!"%(self.name, self.age))
# 实例化类
p = People('darcy', 10, 30)
p.speak()    # darcy说：我10岁!self):

class Student(People):
    grade = ""
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级！"%(self.name, self.age, self.grade))

class Speaker():
    topic = ''
    name = ""
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s,我演讲的主题是%s"%(self.name, self.topic))
# 多重继承
class Sample(Speaker, Student):
    a = ""
    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)

test = Sample("darcy", 25, 80, 4, "python")
# 方法同名，默认调用的是在括号排前的父类的方法
test.speak()    # 我叫darcy,我演讲的主题是python

class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")
c = Child()    # 子类实例
c.myMethod()   # 子类调用重写方法
super(Child, c).myMethod()    # 用子类对象调用父类已被覆盖的方法

class Father(object):
    def __init__(self, name):
        self.name = name
        print("name:%s"%(self.name))
    def getName(self):
        return 'Father' + self.name

class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__(name)
        print("hi!")
        self.name = name
    def getName(self):
        return 'Son,'+self.name
if __name__=='__main__':
    son = Son("python")
    print(son.getName())

class Counter:
    __privateCount = 0    # 私有变量
    publicCount = 0     # 公开变量
    def count(self):
        self.__privateCount += 1
        self.publicCount += 1
        print(self.__privateCount)
sum = Counter()
sum.count()
sum.count()
# print(sum.__privateCount)    # 报错，实例不能访问私有变量
print(sum.publicCount)

class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print("name:", self.name)
        print("url:", self.__url)
    def __foo(self):
        print("这是私有方法！")
    def foo(self):
        print("这是公有方法！")
        self.__foo()
x = Site("百度", "www.baidu.com")
x.who()   # 正常输出
x.foo()   # 正常输出
# x.__foo()  # 报错

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)    # Vector(7, 8)


