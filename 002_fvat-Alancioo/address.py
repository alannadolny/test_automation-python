class Address:
    def __init__(self, street, houseNumber, zipCode, city):
        self.street = street
        self.houseNumber = houseNumber
        self.zipCode = zipCode
        self.city = city

    def getAddress(self):
        return f"{self.street} {self.houseNumber}, {self.zipCode} {self.city}"
