import json


def ui():
    print('———- ICBC Bank ————-')
    print('1.  账户信息')
    print('2.  转账')


def _read(path):
    with open(path) as fin:
        return json.load(fin)


def _write(path, val):
    with open(path, 'w') as fout:
        json.dump(val, fout)


def show_account_info(path):
    info = _read(path)
    print(f"余额: {info['balance']}")


def transfer(sender, receiver, amount):
    amount *= 1.05
    sinfo = _read(sender)
    rinfo = _read(receiver)

    sinfo['balance'] -= amount
    rinfo['balance'] += amount

    _write(sender, sinfo)
    _write(receiver, rinfo)


while True:
    ui()
    uin = int(input('>>> '))
    if uin == 1:
        show_account_info('../alex.json')
    elif uin == 2:
        transfer('../alex.json', '../tesla_corp.json', 95_0000)
