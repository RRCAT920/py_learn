"""
购物车程序开发

根据以下数据结构：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    ....
]
实现功能要求：

1、启动程序后，让用户输入工资，然后进入循环，打印商品列表和编号

2、允许用户根据商品编号选择商品

3、用户选择商品后，检测余额是否够，够就直接扣款，并加入购物车， 不够就提醒余额不足

4、可随时退出，退出时，打印已购买商品和余额
"""
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

salary = int(input('工资：'))

print('-----商品列表-----')
for i, el in enumerate(goods):
    print('[%d]%s: ¥%d' % (i, el['name'], el['price']))

things = []
while True:
    i = int(input('请输入商品编号：'))

    good = goods[i]
    balance = salary - good['price']
    if salary - good['price'] < 0:
        ans = input('余额不足，是否退出(Y/N)：')
        if ans.upper() == 'Y':
            break
    else:
        for i, el in enumerate(things):
            if good['name'] == el['name']:
                things[i]['number'] += 1
                break
        else:
            good['number'] = 1
            things.append(good)
        salary = balance

print('-----清单-----')
print('商品名称\t数量\t价格')
for el in things:
    print('%s\t%d\t%d' % (el['name'], el['number'], el['number'] * el['price']))
print('余额：%d' % salary)
