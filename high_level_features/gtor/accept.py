def g_test():
    while True:
        n = yield  # 接受到的值给n
        print(f'receive from outside: {n}')


gtor = g_test()
gtor.send(None)     # <=> next(gtor)

for i in range(10):
    gtor.send(i)
