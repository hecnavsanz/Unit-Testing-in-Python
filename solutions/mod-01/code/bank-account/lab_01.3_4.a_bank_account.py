# -*- coding: utf-8 -*-
# bank account
class BankAccount:

    # initialize the account balance
    def __init__(self, balance):
        self.__balance = balance

    # put money in the account
    def deposit(self, amount):
        if type(amount) is int and amount >= 0:
            self.__balance += amount
        else:
            return "Only integer(unsigned) amount allowed"
        return self.balance()

    # take money from the account
    def withdraw(self, amount):
        if type(amount) is int and amount >= 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                return "Negative balance not allowed"
        else:
            return "Only integer(unsigned) amount allowed"
        return self.balance()

    # get the account balance
    def balance(self):
        return self.__balance
