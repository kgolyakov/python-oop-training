from account import Account


class Savings(Account):
    def __init__(self, first_name: str, last_name: str, balance=0):
        super(Savings, self).__init__(balance)
        self.__first_name = first_name
        self.__last_name = last_name

    def withdraw(self, amount):
        if amount <= super().balance:
            super(Savings, self).withdraw(amount)

    def __str__(self):
        return f"Owner: {self.name}\n" \
               f"Balance available: {super(Savings, self).balance}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
