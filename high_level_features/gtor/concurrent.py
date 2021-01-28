"""
生成器实现单线程多并发问题
（生产者-消费者模型）
"""


def consumer(name):
    print(f'消费者{name}开始消费')
    while True:
        baozi = yield
        print(f'消费者{name}收到包子{baozi}')


c1 = consumer('C1')
c2 = consumer('C2')
c3 = consumer('C3')
c1.send(None)
c2.send(None)
c3.send(None)

for i in range(10):
    print(f'生产第{i}批包子')
    c1.send(i)
    c2.send(i)
    c3.send(i)
