from abc import ABC


class InvoiceRepository(ABC):
    def __init__(self, data_source=[]):
        self.__data_source = data_source

    def find_by_number(self, number):
        return next((inv for inv in self.data_source if inv.number == number), None)

    def add(self, invoice):
        if not self.find_by_number(invoice.number):
            self.__data_source.append(invoice)

    def delete(self, invoice):
        self.__data_source.remove(invoice)

    def update(self, old_invoice, new_invoice):
        self.delete(old_invoice)
        self.add(new_invoice)

    def get_next_number(self):
        if len(self.__data_source) == 0:
            return 1
        else:
            return self.__data_source[len(self.__data_source) - 1].number + 1

    @property
    def data_source(self):
        return self.__data_source
