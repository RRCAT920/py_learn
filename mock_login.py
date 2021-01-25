"""
模拟登陆
1.用户输入帐号密码进行登录
2.用户信息保存在文件内
3.密码输入错误三次后锁定用户，下次再登录，检测到是这个用户也登录不了
(只处理存在的用户)
"""
import sys

file = 'user_info.txt'
info = []
with open(file) as f:
    for line in f:
        user = line.strip().split(':')
        item = {'username': user[0], 'password': user[1]}
        if len(user) == 3:
            item['lock'] = None
        info.append(item)

username = input('Username: ')
i = -1
for _ in range(3):
    pwd = input('Password: ')
    for index, item in enumerate(info):
        if username == item['username']:
            i = index
            if 'lock' in item:
                print(f'{username}已锁定')
                sys.exit(0)
            if pwd == item['password']:
                print('登录成功')
                sys.exit(0)

info[i]['lock'] = None
with open(file, 'w') as f:
    for item in info:
        line = '{username}:{password}'.format_map(item)
        if 'lock' in item:
            line += ':'
        f.write(line + '\n')
