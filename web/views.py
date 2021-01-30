
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
