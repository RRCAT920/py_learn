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


from jinja2 import Template
def get_dict(env):
    user_dict = {
        'username': 'jack',
        'age': 18,
    }

    with open('templates/get_dict.html', 'r') as f:
        data = f.read()
    tmpl = Template(data)
    return tmpl.render(user=user_dict)


import pymysql
def get_user(env):
    """
    从数据库获取数据，借助模版引擎处理数据，再发送给浏览器
    :param env:
    :return:
    """
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='tkl19981125',
        database='user_db',
        charset='utf8',
        autocommit=True
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from t_account'
    row_count = cursor.execute(sql)
    data_list = cursor.fetchall()   # List[Dict]

    with open('templates/get_data.html', 'r') as f:
        data = f.read()
    tmpl = Template(data)
    return tmpl.render(user_list=data_list)


if __name__ == '__main__':
    get_user(123)