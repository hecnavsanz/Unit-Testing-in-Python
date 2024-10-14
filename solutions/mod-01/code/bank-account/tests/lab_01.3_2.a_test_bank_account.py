# -*- coding: utf-8 -*-

from bank_account import BankAccount


class TestBankAccount:

    # test a negative deposit in the bank account to raise an exception
    def test_deposit(self):
        ba = BankAccount()
        ba.balance = 1000
        assert ba.deposit(-100) == "Only integer(unsigned) amount allowed"

        # another examples to raise an exception: string or float amount
        # assert ba.deposit("100") == "Only integer(unsigned) amount allowed"
        # assert ba.deposit(100.00) == "Only integer(unsigned) amount allowed"
