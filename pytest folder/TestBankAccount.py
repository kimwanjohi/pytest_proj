# test_bank_account.py

import pytest;
from bank_account import BankAccount

def test_initial_balance():
    account = BankAccount(1000)
    assert account.get_balance() == 1000

def test_deposit():
    account = BankAccount()
    account.deposit(500)
    assert account.get_balance() == 500

def test_deposit_invalid_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-100)

def test_withdraw():
    account = BankAccount(1000)
    account.withdraw(300)
    assert account.get_balance() == 700

def test_withdraw_invalid_amount():
    account = BankAccount(1000)
    with pytest.raises(ValueError):
        account.withdraw(0)
    with pytest.raises(ValueError):
        account.withdraw(-50)

def test_withdraw_overdraft_limit():
    account = BankAccount(0, overdraft_limit=-200)
    account.withdraw(150)
    assert account.get_balance() == -150

    with pytest.raises(ValueError):
        account.withdraw(100)  # Would go beyond -200

def test_overdraft_limit_exceeded():
    account = BankAccount(100, overdraft_limit=-100)
    with pytest.raises(ValueError):
        account.withdraw(250)  # Would go to -150
