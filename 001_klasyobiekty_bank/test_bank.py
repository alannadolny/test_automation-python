import unittest
import bank
import datetime


class TestBank(unittest.TestCase):
    def test_unable_to_withdraw(self):
        account = bank.BankAccount()
        result = account.withdraw(10)
        self.assertFalse(result)

    def test_withdraw_less_than_0(self):
        account = bank.BankAccount()
        result = account.withdraw(-2)
        self.assertFalse(result)

    def test_deposit(self):
        account = bank.BankAccount()
        result = account.deposit(10)
        self.assertEqual(result, 10)

    def test_deposit_less_than_0(self):
        account = bank.BankAccount()
        result = account.deposit(-2)
        self.assertFalse(result)

    def test_unable_to_transfer(self):
        firstAccount = bank.BankAccount()
        secondAccount = bank.BankAccount()
        result = firstAccount.bankTransfer(20, secondAccount)
        self.assertFalse(result)

    def test_transfer_less_than_0(self):
        firstAccount = bank.BankAccount()
        secondAccount = bank.BankAccount()
        result = firstAccount.bankTransfer(-5, secondAccount)
        self.assertFalse(result)

    def test_transfer(self):
        firstAccount = bank.BankAccount()
        secondAccount = bank.BankAccount()
        firstAccount.deposit(5)
        result = firstAccount.bankTransfer(5, secondAccount)
        self.assertEqual(result, (0, 5))

    def test_empty_history(self):
        account = bank.BankAccount()
        result = account.history.getHistory('1990-01-01', '1990-01-01')
        self.assertEqual(result, [])

    def test_history_deposit_and_withdraw(self):
        account = bank.BankAccount()
        account.deposit(10)
        account.withdraw(10)
        result = account.history.getHistory(datetime.date.today(), datetime.date.today())
        self.assertEqual(result, ["Deposit: +10$ at: " + str(datetime.date.today()),
                                  "Withdraw: -10$ at: " + str(datetime.date.today())])

    def test_history_transfer(self):
        firstAccount = bank.BankAccount()
        secondAccount = bank.BankAccount()
        firstAccount.deposit(5)
        firstAccount.bankTransfer(5, secondAccount)
        result = firstAccount.history.getHistory(datetime.date.today(), datetime.date.today())
        result2 = secondAccount.history.getHistory(datetime.date.today(), datetime.date.today())
        self.assertEqual(result, ["Deposit: +5$ at: " + str(datetime.date.today()),
                                  "Transfer: -5$ at: " + str(datetime.date.today())])
        self.assertEqual(result2, ["Transfer: +5$ at: " + str(datetime.date.today())])

    def test_checkAccount(self):
        account = bank.BankAccount()
        result = account.checkAccount()
        self.assertEqual(result, "You have 0$")

    def test_checkAccount_after_deposit(self):
        account = bank.BankAccount()
        account.deposit(10)
        result = account.checkAccount()
        self.assertEqual(result, "You have 10$")


if __name__ == '__main__':
    unittest.main()
