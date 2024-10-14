# -*- coding: utf-8 -*-

# bank account
class BankAccount:

    # the account balance
    balance = 0

    # put money in the account
    def deposit(self, amount):
        if type(amount) is int and amount >= 0:
            self.balance += amount
        else:
            return "Only integer(unsigned) amount allowed"
        return self.balance
