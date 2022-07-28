import worker
import exceptions


class OfficeWorker(worker.Worker):
    def __init__(self, firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company,
                 iq):
        super().__init__(firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company)
        self.officeIdentifier = company.generatingOfficeIdentifier()
        self.iq = iq

    @property
    def iq(self):
        return self.__iq

    @iq.setter
    def iq(self, p):
        if p < 70 or p > 150:
            raise exceptions.IqMustBeBetween70And150
        else:
            self.__iq = p
