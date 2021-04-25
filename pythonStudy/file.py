import os
import time
#
# s = os.getcwd()
# print(s)    # E:\LearnPython\pythonStudy
#
# #  文件的名称,模式
# f = open('liyuhuan.txt', "r")
# # print(f)
# print("======")
#
# folder = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
#
# os.makedirs(r'%s/%s' %(os.getcwd(), folder))

# a = os.path.isfile("E:\LearnPython\pythonStudy\liyuhuan.txt")
# print(a)   # True
# a = os.path.isfile("E:\LearnPython\pythonStudy")
# print(a)   # False
# list = os.listdir("E:\LearnPython\pythonStudy")
# print(list)

def getDirList(p):
    p = str(p)
    if p == "":
        return []
    p = p.replace("/", "\\")
    if p[-1] != "\\":
        p = p + "\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isdir(p + x)]
    return b


print(getDirList("E:\LearnPython\pythonStudy"))    # ['2021-04-25_17-31-12']


def getFileList(p):
    p = str(p)
    if p == "":
        return []
    p = p.replace("/", "\\")
    if p[-1] != "\\":
        p = p + "\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isfile(p + x)]
    return b


print(getFileList("E:\LearnPython\pythonStudy"))
