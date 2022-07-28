import address
import random


class Company:
    def __init__(self):
        self.workersId = []
        self.officeIdentifier = []

    def generateId(self):
        while True:
            id = random.randint(1, 10000)
            if id not in self.workersId:
                self.workersId.append(id)
                break
        return id

    def generatingOfficeIdentifier(self):
        while True:
            id = random.randint(1, 10000)
            if id not in self.officeIdentifier:
                self.officeIdentifier.append(id)
                return id


class Worker:
    def __init__(self, firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.experience = experience
        self.companyAddress = address.Address(street, buildingNumber, apartmentNumber, city)
        self.workerId = company.generateId()
