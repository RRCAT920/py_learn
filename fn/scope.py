"""
全局变量和局部变量
"""


def change_without_global():
    name = "Jack"
    print(name)


def change():
    global name
    name = "Jack"
    print(name)


name = "Michael"
change_without_global()
print(name)
change()
print(name)
