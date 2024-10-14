# -*- coding: utf-8 -*-

from bank_account import BankAccount


class TestBankAccount:
    # different bank account test cases
    test_cases = [
        {"balance": 100,
         "deposit_amount": 10,
         "withdraw_amount": 30,
         "initialization_expected": 100,
         "deposit_expected": 110,
         "withdraw_expected": 70},
        {"balance": 500,
         "deposit_amount": 450,
         "withdraw_amount": 30,
         "initialization_expected": 500,
         "deposit_expected": 950,
         "withdraw_expected": 470},
        {"balance": 300,
         "deposit_amount": -305,
         "withdraw_amount": 30,
         "initialization_expected": 300,
         "deposit_expected": "Only integer(unsigned) amount allowed",
         "withdraw_expected": 270},
        {"balance": 300,
         "deposit_amount": 100,
         "withdraw_amount": -40,
         "initialization_expected": 300,
         "deposit_expected": 400,
         "withdraw_expected": "Only integer(unsigned) amount allowed"},
        {"balance": 200,
         "deposit_amount": 250,
         "withdraw_amount": 500,
         "initialization_expected": 200,
         "deposit_expected": 450,
         "withdraw_expected": "Negative balance not allowed"},
        {"balance": "500",
         "deposit_amount": 250,
         "withdraw_amount": 300,
         "initialization_expected": "Negative or alphanumeric balance not allowed",
         "deposit_expected": "Negative or alphanumeric balance not allowed",
         "withdraw_expected": "Negative or alphanumeric balance not allowed"},
        {"balance": -500,
         "deposit_amount": 250,
         "withdraw_amount": 300,
         "initialization_expected": "Negative or alphanumeric balance not allowed",
         "deposit_expected": "Negative or alphanumeric balance not allowed",
         "withdraw_expected": "Negative or alphanumeric balance not allowed"},
        {"balance": 500,
         "deposit_amount": "250",
         "withdraw_amount": 300,
         "initialization_expected": 500,
         "deposit_expected": "Only integer(unsigned) amount allowed",
         "withdraw_expected": 200},
        {"balance": 500,
         "deposit_amount": 250,
         "withdraw_amount": "300",
         "initialization_expected": 500,
         "deposit_expected": 750,
         "withdraw_expected": "Only integer(unsigned) amount allowed"}
    ]

    # test bank account initialization test cases
    def test_initialization(self):

        for test in self.test_cases:
            ba = BankAccount(test["balance"])
            assert ba.balance() == test["initialization_expected"]
            # assert isinstance(ba.balance(), int)

    # test bank account deposit test cases
    def test_deposit(self):

        for test in self.test_cases:
            ba = BankAccount(test["balance"])
            assert ba.deposit(test["deposit_amount"]) == test["deposit_expected"]

    # test bank account withdraw test cases
    def test_withdraw(self):

        for test in self.test_cases:
            ba = BankAccount(test["balance"])
            assert ba.withdraw(test["withdraw_amount"]) == test["withdraw_expected"]
