# -*- coding: utf-8 -*-

from bank_account import BankAccount


class TestBankAccount:

    # test bank account deposit test cases
    def test_deposit(self):

        # different bank account test cases
        test_cases = [
            {"balance": 100,
             "deposit_amount": 10,
             "deposit_expected": 110},
            {"balance": 300,
             "deposit_amount": -305,
             "deposit_expected": "Only integer(unsigned) amount allowed"},
        ]

        for test in test_cases:
            ba = BankAccount(test["balance"])
            assert ba.deposit(test["deposit_amount"]) == test["deposit_expected"]

    # test bank account withdraw test cases
    def test_withdraw(self):

        # different bank account test cases
        test_cases = [
            {"balance": 100,
             "withdraw_amount": 30,
             "withdraw_expected": 70},
            {"balance": 200,
             "withdraw_amount": 500,
             "withdraw_expected": "Negative balance not allowed"},
        ]

        for test in test_cases:
            ba = BankAccount(test["balance"])
            assert ba.withdraw(test["withdraw_amount"]) == test["withdraw_expected"]
