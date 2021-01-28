"""
给函数传递列表
"""

names = ["alex", "jack"]


def change(lst):
    lst.append("harry")


change(names)
print(names)

name = "harrison"


def change_str(string):
    string = "marry"


change_str(name)
print(name)