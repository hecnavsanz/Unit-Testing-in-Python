# -*- coding: utf-8 -*-
from bank_account import BankAccount


class TestBankAccount:

    # test a deposit in the bank account
    def test_deposit(self):
        ba = BankAccount()
        ba.balance = 1000
        assert ba.deposit(100) == 1100
