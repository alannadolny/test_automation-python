import address
import random


class Bank(address.Address):
    def __init__(self, name, street, houseNumber, zipCode, city):
        super().__init__(street, houseNumber, zipCode, city)
        self.name = name
        self.accountNumber = random.choices(range(0, 9), k=26)

    def getAccountNumber(self):
        accountNumber = ""
        for i in self.accountNumber:
            accountNumber += str(i)
        return accountNumber

    def getAccountDetails(self):
        return f"Numer konta: {self.getAccountNumber()}, Oddział: {self.name} - {self.street} {self.houseNumber}, {self.zipCode} {self.city}"
