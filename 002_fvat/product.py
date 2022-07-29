import exceptions


class Product:
    def __init__(self, name, price, vat, quantity):
        self.name = name
        self.beforeTax = price
        self.vat = vat
        self.quantity = quantity
        self.afterTax = round(price * quantity * vat, 2) + price * quantity

    @property
    def beforeTax(self):
        return self.__beforeTax

    @property
    def vat(self):
        return self.__vat

    @property
    def quantity(self):
        return self.__quantity

    @beforeTax.setter
    def beforeTax(self, p):
        if p <= 0:
            raise exceptions.PriceLowerThanZeroError
        else:
            self.__beforeTax = p

    @vat.setter
    def vat(self, p):
        if p > 1 or p < 0:
            raise exceptions.VatMustBeBetweenZeroAndOneError
        else:
            self.__vat = p

    @quantity.setter
    def quantity(self, p):
        if p <= 0:
            raise exceptions.QuantityLowerThanZeroError
        else:
            self.__quantity = p

    def getPriceForInvoice(self):
        return f"{self.name}: {self.quantity}szt. cena jednostkowa netto: {self.beforeTax}zł," \
               f" cena netto: {self.beforeTax * self.quantity}zł, VAT: {self.vat * 100}%, wartość VAT:" \
               f" {round(self.beforeTax * self.quantity * self.vat, 2)}zł, cena brutto: {round(self.afterTax, 2)}zł"

    def getValue(self):
        return round(self.afterTax, 2)
