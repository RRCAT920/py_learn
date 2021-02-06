def withdraw(principal, amount, rate):
    pay = amount * rate
    if amount <= principal - pay:
        return principal - pay - amount

    print('金额不足，无法提现')