from abc import ABC
from Invoice import Invoice


class Shop(ABC):
    def __init__(self, repository=None, storehouse=None):
        self.__invoice_repository = repository
        self.__storehouse = storehouse

    def buy(self, customer, items_list):
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list)
        self.invoice_repository.add(invoice)
        for product in items_list:
            self.storehouse.getFromStorehouse(product)
        return invoice

    def returning_goods(self, invoice, partial_returning=[]):
        if partial_returning:
            not_returned_goods = []
            for product in invoice.items:
                if product not in partial_returning:
                    not_returned_goods.append(product)
            new_invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=invoice.customer,
                                  items=not_returned_goods)
            for product in partial_returning:
                self.storehouse.addToStorehouse({'name': product, 'quantity': 1})
            self.invoice_repository.update(invoice, new_invoice)

        else:
            if self.invoice_repository.find_by_number(invoice.number):
                for product in invoice.items:
                    self.storehouse.addToStorehouse({'name': product, 'quantity': 1})
                self.invoice_repository.delete(invoice)
                return True
            else:
                return False

    @property
    def invoice_repository(self):
        return self.__invoice_repository

    @property
    def storehouse(self):
        return self.__storehouse
