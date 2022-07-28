from abc import ABC
from exceptions import OutOfStore, InvalidProductData


class Storehouse(ABC):
    def __init__(self, productsList=[]):
        self.productsList = productsList

    def addToStorehouse(self, product):
        ifExists = False
        if 'name' in product and 'quantity' in product:
            for i in range(0, len(self.productsList)):
                if self.productsList[i]['name'] == product['name']:
                    ifExists = True
                    self.productsList[i] = {'name': product['name'],
                                            'quantity': self.productsList[i]['quantity'] + product['quantity']}
                    return self.productsList
            if not ifExists:
                self.productsList.append(product)
                return self.productsList
        else:
            raise InvalidProductData

    def getFromStorehouse(self, product):
        ifExists = False
        for i in range(0, len(self.productsList)):
            if self.productsList[i]['name'] == product:
                ifExists = True
                if self.productsList[i]['quantity'] == 0:
                    raise OutOfStore
                else:
                    if self.productsList[i]['quantity'] == 1:
                        self.productsList = list(
                            filter(lambda productFromStorehouse: productFromStorehouse != self.productsList[i],
                                   self.productsList))
                        return self.productsList
                    else:
                        self.productsList[i] = {'name': product, 'quantity': self.productsList[i]['quantity'] - 1}
                        return self.productsList
        if not ifExists:
            raise OutOfStore
