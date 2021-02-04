import json
from datetime import datetime
import hashlib

"""
只有一个文件，故不会锁定其他用户
"""

file = ''
info = None
for _ in range(3):
    uin = input('Username: '), input('Password: ')

    file = f'{uin[0]}.json'
    with open(file, 'r+') as fio:
        info = json.load(fio)
        password = info['password']

        if hashlib.md5(uin[1].encode()).hexdigest() == password:
            if info['status']:
                print('用户已锁定')
                break
            if datetime.today() > datetime.strptime(info['expire_date'],
                                                    '%Y-%m-%d'):
                print('用户已过期')
                break

            print('登录成功')
            break
else:
    info['status'] = 1
    with open(file, 'w') as fout:
        json.dump(info, fout)
