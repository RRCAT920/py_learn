"""
使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
"""
for i in range(100, -2, -1):
    if i >= 50:
        print(i)
    else:
        print(49 - i)
