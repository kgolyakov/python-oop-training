class Account:
    accounts_num = 0

    def __init__(self, initial_amount=0):
        self.__balance = initial_amount
        self.__id = self.__class__.accounts_num
        self.__class__.accounts_num += 1

    def withdraw(self, amount: int):
        if 0 <= amount:
            self.__balance -= amount

    def deposit(self, amount: int):
        if amount >= 0:
            self.__balance += amount

    @property
    def balance(self):
        return self.__balance

    @property
    def id(self):
        return self.__id
