import address


class Customer:
    def __init__(self, firstName, lastName, street, houseNumber, zipCode, city):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address.Address(street, houseNumber, zipCode, city)

    def getCustomer(self):
        return f"Nabywca: \n{self.firstName} {self.lastName}, {self.address.getAddress()}"
