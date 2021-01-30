from views import *

"""
路由与视图函数的对应关系
"""
urls = [
    ('/index', index),
    ('/login', login),
]


# def viewfn(fn):
#     urls.append((fn.__name__, fn))
