from views import *

"""
路由与视图函数的对应关系
"""
urls = [
    ('/index', index),
    ('/login', login),
    ('/get_time', get_time)
]


# def viewfn(fn):
#     urls.append((fn.__name__, fn))
