# -*- coding: utf-8 -*-

# bank account
class BankAccount:

    # initialize the account balance
    def __init__(self, balance):
        if type(balance) is int and balance >= 0:
            self.__balance = balance
        else:
            self.__balance = "Negative or alphanumeric balance not allowed"

    # put money in the account
    def deposit(self, amount):
        if type(self.__balance) is int and int(self.__balance) >= 0:
            if type(amount) is int and amount >= 0:
                self.__balance += amount
            else:
                return "Only integer(unsigned) amount allowed"
        else:
            return "Negative or alphanumeric balance not allowed"
        return self.balance()

    # take money from the account
    def withdraw(self, amount):
        if type(self.__balance) is int and int(self.__balance) >= 0:
            if type(amount) is int and amount >= 0:
                if amount <= self.__balance:
                    self.__balance -= amount
                else:
                    return "Negative balance not allowed"
            else:
                return "Only integer(unsigned) amount allowed"
        else:
            return "Negative or alphanumeric balance not allowed"
        return self.balance()

    # get the account balance
    def balance(self):
        return self.__balance
