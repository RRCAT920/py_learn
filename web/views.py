"""
视图函数（后端业务逻辑）
"""


def index(env):
    return 'index'


def login(env):
    return 'login'


def error(env):
    return '404 error'


def html(env):
    # 可以写视图解析器
    with open('templates/index.html', 'r') as f:
        return f.read()


import datetime
def get_time(env):
    now = datetime.datetime.now().strftime('%Y-%m-%d %X')
    # 如何将数据传递给html
    with open('templates/mytime.html', 'r') as f:
        data = f.read()  # html页面内容
    data = data.replace('show_time_here', now)  # 简易模版引擎
    return data
