import os
from datetime import datetime


def log(user, operation, info):
    with open('logs/bank.log', 'a') as fout:
        now = datetime.now().strftime('%Y%m%d %X')
        msg = f'{now} {user} {operation} {info}.'
        fout.write(msg + os.linesep)
