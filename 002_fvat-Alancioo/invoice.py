import datetime
import random


class Invoice:
    def __init__(self, customer, seller, paymentDate, sellDate):
        self.id = f"{random.randint(1, 10000)}/{datetime.date.today().month}/{datetime.date.today().year}"
        self.customer = customer
        self.seller = seller
        self.products = []
        self.value = 0
        self.paymentDate = datetime.date(int(paymentDate.split("-")[2]), int(paymentDate.split("-")[1]),
                                         int(paymentDate.split("-")[0]))
        self.sellDate = datetime.date(int(sellDate.split("-")[2]), int(sellDate.split("-")[1]),
                                      int(sellDate.split("-")[0]))
        self.invoiceDate = datetime.date.today()

    def addProduct(self, product):
        self.products.append(product.getPriceForInvoice())
        self.value = self.value + product.getValue()
        return self.products

    def getProducts(self):
        products = ""
        for i in self.products:
            products += i + "\n"
        return products

    def getInvoice(self):
        return f"Numer faktury: {self.id} \n{self.seller.getSeller()} \n{self.customer.getCustomer()} \nProdukty: \n{self.getProducts()}" \
               f"Wartość całkowita: {round(self.value, 2)}zł \nData sprzedaży: {self.sellDate} \nData zapłaty: {self.paymentDate} \n" \
               f"Data wystawienia faktury: {self.invoiceDate}"
