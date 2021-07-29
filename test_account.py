from account import Account
from savings import Savings

if __name__ == '__main__':
    a = Account(100500)
    a.deposit(15000)
    a.withdraw(10000)
    print(a.balance)
    a.withdraw(100000000000)
    print(a.balance)
    b = Account(0)
    print(b.balance)
    print(a.balance)
    a.withdraw(-100)
    print(a.balance)
    a.withdraw(105500)
    print(a.balance)
    print(a.id)
    print(b.id)
    c = Savings("A", "B", 15)
    print(c)
    c.withdraw(16)
    print(c.name, c.balance)
    c.last_name = "C"
    print(c.name)