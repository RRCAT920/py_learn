grade = int(input('成绩：'))

if grade < 0 or grade > 100:
    raise ValueError('成绩应该在0-100之间')
elif grade < 40:
    print('E')
elif grade < 60:
    print('D')
elif grade < 80:
    print('C')
elif grade < 90:
    print('B')
else:
    print('A')