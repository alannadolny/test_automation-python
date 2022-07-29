import random
import customer


class Seller(customer.Customer):
    def __init__(self, firstName, lastName, street, houseNumber, zipCode, city, bankAccount, companyName):
        super().__init__(firstName, lastName, street, houseNumber, zipCode, city)
        self.nipNumber = random.choices(range(0, 9), k=10)
        self.bankAccount = bankAccount
        self.companyName = companyName

    def getNip(self):
        nip = ""
        for i in self.nipNumber:
            nip += str(i)
        return nip

    def getSeller(self):
        return f"Sprzedawca: \n{self.companyName} - {self.firstName} {self.lastName}, {self.address.getAddress()}," \
               f" NIP: {self.getNip()}, konto bankowe: {self.bankAccount.getAccountDetails()}"
