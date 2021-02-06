from script import start
from logs import log

while True:
    start.ui()
    uin = int(input('>>> '))
    if uin == 1:
        start.show_account_info()
    elif uin == 2:
        amount = float(input('转账金额 >>> '))
        user = input('转账对象 >>> ')
        start.transfer(user, amount)
    elif uin == 3:
        amount = float(input('提现金额 >>> '))
        start.cashing(amount)
    elif uin == 4:
        break
