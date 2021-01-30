from wsgiref.simple_server import make_server
from urls import *
from views import *


def app(env, resp):
    """
    处理器
    :param env: 请求相关的数据(wsgi模块将其封装成字典)
    :param resp: 响应相关的数据
    :return: 给浏览器的数据
    """
    resp('200 OK', [])
    path = env['PATH_INFO']
    fn = None
    for url in urls:
        if path == url[0]:
            fn = url[1]
            break

    res = (fn if fn else error)(env)
    return [res.encode()]


if __name__ == '__main__':
    '''
    实时监听localhost:9090
    app处理请求
    '''
    with make_server('127.0.0.1', 9090, app) as srv:
        srv.serve_forever()  # 启动服务器
