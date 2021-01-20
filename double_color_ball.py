"""
双色球彩票 选购程序

1. 先让用户依次选择6个红球，再选择2个蓝球，最后统一打印用户选择的球号。
2. 确保用户不能选择重复的，选择的数不能超出范围。
"""
print('Welcome to lottery station')
red_balls = []
blue_balls = []
i = 1
while i <= 6:
    n = int(input('[%d]select red ball:' % i))
    if n < 1 or n > 32:
        print('only can select n between 1-32')
    elif n in red_balls:
        print('number %d is already exist in red ball list' % n)
    else:
        red_balls.append(n)
        i += 1

i = 1
while i <= 2:
    n = int(input('[%d]select blue ball:' % i))
    if n < 1 or n > 16:
        print('only can select n between 1-16')
    elif n in blue_balls:
        print('number %d is already exist in blue ball list' % n)
    else:
        blue_balls.append(n)
        i += 1

print('\n')
print('Red ball: %s' % red_balls)
print('Blue ball: %s' % blue_balls)
print('Good Luck.')
