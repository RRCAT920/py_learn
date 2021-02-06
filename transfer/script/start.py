import functools
import json
from core import withdraw
from core import validation
from logs import log

_signed = False
_file = ''


def login(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        global _signed, _file
        while True:
            if _signed:
                return fn(*args, **kwargs)
            _signed, _file = validation.sign()

    return wrapper


def ui():
    print('———- ICBC Bank ————-')
    print('1.  账户信息')
    print('2.  转账')
    print('3.  提现')
    print('4.  退出')


def _read(path):
    with open(path) as fin:
        return json.load(fin)


def _write(path, val):
    with open(path, 'w') as fout:
        json.dump(val, fout)


@login
def show_account_info():
    info = _read(_file)
    print(f"余额: {info['balance']}")
    log.log(_file.split('.')[0], 'check', 'checked account')


@login
def transfer(receiver, amount):
    path = f'{receiver}.json'
    interest = amount * 0.05
    sinfo = _read(_file)
    rinfo = _read(path)

    sinfo['balance'] -= amount + interest
    rinfo['balance'] += amount + interest

    _write(_file, sinfo)
    _write(path, rinfo)

    info = f'transferred to [{receiver}] with amount RMB{amount}, interest is RMB{interest}'
    log.log(_file.split('.')[0], 'transfer', info)


@login
def cashing(amount):
    info = _read(_file)
    left = withdraw.withdraw(info['balance'] + info['credits'], amount, 0.05)
    if left is None:
        return

    if left > info['balance']:
        info['credits'] = left - info['balance']
    else:
        info['credits'] = 0
        info['balance'] = left
    _write(_file, info)

    info = f'withdraw cash RMB{amount}, interest is RMB{amount * 0.05}'
    log.log(_file.split('.')[0], 'withdraw', info)
