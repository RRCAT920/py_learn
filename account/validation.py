import json
from datetime import datetime
import hashlib


def login():
    file = ''
    info = None
    last_user = None
    count = 0
    while count < 3:
        uin = input('Username: '), input('Password: ')
        # 如果更改用户名则重新记数
        if last_user is None:
            last_user = uin[0]
        if last_user == uin[0]:
            count += 1
        else:
            count = 0

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
        print(f'您登录超过{count}次，已锁定{last_user}')
        info['status'] = 1
        with open(file, 'w') as fout:
            json.dump(info, fout)


if __name__ == '__main__':
    login()