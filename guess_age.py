import random

"""
猜年龄游戏

要求：
1.允许用户最多尝试3次
2.3次没猜对就退出，退出后询问用户是否继续
3.猜对就打印恭喜
"""
n = random.randint(0, 200)
count = 0
while True:
    count += 1
    guess = int(input('猜年龄(%s): ' % count))
    if guess == n:
        break

    if count == 3:
        ans = input('是否继续(Y/N)：')
        if ans.lower() == 'n':
            break
        count = 0
