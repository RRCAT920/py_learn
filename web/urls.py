from views import *

"""
路由与视图函数的对应关系
"""
urls = [
    ('/index', index),
    ('/login', login),
    ('/get_time', get_time),
    ('/get_dict', get_dict),
    ('/get_user', get_user),
]


# def viewfn(fn):
#     urls.append((fn.__name__, fn))
