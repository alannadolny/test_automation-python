import worker
import exceptions


class PhysicalWorker(worker.Worker):
    def __init__(self, firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company,
                 strength):
        super().__init__(firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company)
        self.strength = strength

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, p):
        if p < 1 or p > 100:
            raise exceptions.StrengthMustBeBetween1And100
        else:
            self.__strength = p
