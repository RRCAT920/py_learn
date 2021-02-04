"""
eval
需要注意两种特殊情况
-a
a.b
"""
import re


def cal0(expr):
    high = re.compile(r'\d+(\.\d+)?[\*\/]\-?\d+(\.\d+)?')  # 乘除算式pattern
    match = high.search(expr)
    while match:
        formula = match.group()
        if '*' in formula:
            a, b = formula.split('*')
            val = float(a) * float(b)
        elif '/' in formula:
            a, b = formula.split('/')
            val = float(a) / float(b)
        expr = expr.replace(formula, str(val))
        match = high.search(expr)

    def _stdize(expr):
        d = {
            '++': '+',
            '--': '+',
            '+-': '-',
            '-+': '+'
        }
        flag = True
        while flag:
            for opr in d:
                expr = expr.replace(opr, d[opr])

            for opr in d:
                if opr not in expr:
                    flag = False
                    break

        return expr

    return _stdize(expr)


def cal1(expr):
    number = re.compile('[\+\-]?\d+(?:\.\d+)?')
    numbers = number.findall(expr)
    s = 0
    for n in numbers:
        s += float(n)
    return s


def cal(expr):
    expr = cal0(expr)
    return cal1(expr)


def eval_(expr):
    par = re.compile(r'\([^()]+\)')
    match = par.search(expr)
    while match:
        res = match.group()
        repl = str(cal(res[1:-1]))
        expr = expr.replace(res, repl)
        match = par.search(expr)
    return cal(expr)


expr = '1 - 2 *( (60-30 +(-40/5)* (9-2*5/3 + 7 /3*99/4*2998 +10* 568/14 )) - (-4*3)/ (16-3*2) )'
expr = ''.join(expr.split())
print(eval(expr))
print(eval_(expr))
print(eval_('1-1*-1'))
print(eval_('1++-+-+2'))
