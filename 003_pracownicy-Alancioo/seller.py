import worker
import exceptions
import re


class Seller(worker.Worker):
    def __init__(self, firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company,
                 effectiveness, provision):
        super().__init__(firstName, lastName, age, experience, street, buildingNumber, apartmentNumber, city, company)
        self.effectiveness = effectiveness
        self.provision = provision

    @property
    def effectiveness(self):
        return self.__effectiveness

    @effectiveness.setter
    def effectiveness(self, p):
        if p not in ('low', 'mid', 'high'):
            raise exceptions.EffectivenessMustBeLowOrMidOrHigh
        else:
            self.__effectiveness = p

    @property
    def provision(self):
        return self.__provision

    @provision.setter
    def provision(self, p):
        try:
            if int(p) < 0 or int(p) > 100:
                raise exceptions.ProvisionMustBeBetween0And100
            else:
                self.__provision = p
        except ValueError:
            raise exceptions.ProvisionMustBeANumber
