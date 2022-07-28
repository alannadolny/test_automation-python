import history


def getDate(date):
    return int(str(date).split("-")[0]) * 10000 + int(str(date).split("-")[1]) * 100 + int(str(date).split("-")[2])


class BankAccount:
    def __init__(self):
        self.money = 0
        self.history = history.History()

    def withdraw(self, money):
        if self.money < money or money < 0:
            return False
        else:
            self.money -= money
            self.history.addWithdraw(money)
            return self.money

    def deposit(self, money):
        if money < 0:
            return False
        else:
            self.money += money
            self.history.addDeposit(money)
            return self.money

    def bankTransfer(self, money, destinationAccount):
        if self.money < money or money < 0:
            return False
        else:
            self.money -= money
            self.history.addSendedTransfer(money)
            destinationAccount.money += money
            destinationAccount.history.addReceivedTransfer(money)
            return self.money, destinationAccount.money

    def checkAccount(self):
        return f"You have {self.money}$"
