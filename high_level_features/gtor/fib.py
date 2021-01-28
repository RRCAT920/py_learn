from typing import *


def fib(n: int) -> Generator:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


fib_gtor = fib(20)
print(next(fib_gtor))
