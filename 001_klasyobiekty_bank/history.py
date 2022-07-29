import datetime
import bank

class History:
    def __init__(self):
        self.history = []

    def addDeposit(self, money):
        self.history.append(f"Deposit: +{money}$ at: {datetime.date.today()}")

    def addWithdraw(self, money):
        self.history.append(f"Withdraw: -{money}$ at: {datetime.date.today()}")

    def addReceivedTransfer(self, money):
        self.history.append(f"Transfer: +{money}$ at: {datetime.date.today()}")

    def addSendedTransfer(self, money):
        self.history.append(f"Transfer: -{money}$ at: {datetime.date.today()}")

    def getHistory(self, start, end):
        choseHistory = []
        for i in range(0, len(self.history)):
            if bank.getDate(start) <= bank.getDate(self.history[i].split(" ")[3]) <= bank.getDate(end):
                choseHistory.append(self.history[i])
        return choseHistory
