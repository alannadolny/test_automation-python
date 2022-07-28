class Address:
    def __init__(self, street, buildingNumber, apartmentNumber, city):
        self.street = street
        self.buildingNumber = buildingNumber
        self.apartmentNumber = apartmentNumber
        self.city = city

    def getAddress(self):
        return f'address: {self.city}, {self.street} {self.buildingNumber}/{self.apartmentNumber}'
