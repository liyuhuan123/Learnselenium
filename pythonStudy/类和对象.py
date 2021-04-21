# 类和对象:面向对象编程
# 人:张三,李四,王五
# 人是类
# 张三,李四,王五,是具体的对象
class Person:
    def _init_(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday
    def say(self, word):
        print(f'{self.name}说:"{word}"')

zhang_shan = Person('张三', '男', '20000202')
li_si = Person('李四','女','20000202')
zhang_shan.say('你好')
li_si.say('你也好')