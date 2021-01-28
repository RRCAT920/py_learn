"""
global声明会创建全局变量
"""


def foo():
    global name
    name = "Jack"
    print(name)


def bar():
    global name
    name = "Harry"
    print(name)


foo()
bar()
print(name)
