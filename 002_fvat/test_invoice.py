import unittest
import address
import customer
import bank
import seller
import product
import invoice
import datetime
import exceptions


class TestInvoice(unittest.TestCase):
    def test_get_address(self):
        address_test = address.Address("test_street", "test_houseNumber", "test_zipCode", "test_city")
        result = address_test.getAddress()
        self.assertEqual("test_street test_houseNumber, test_zipCode test_city", result)

    def test_get_customer(self):
        customer_test = customer.Customer("test_firstname", "test_lastname", "test_street",
                                          "test_houseNumber", "test_zipCode", "test_city")
        result = customer_test.getCustomer()
        self.assertEqual("Nabywca: \ntest_firstname test_lastname, test_street test_houseNumber,"
                         " test_zipCode test_city", result)

    def test_account_number(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        result = bankAccount.getAccountNumber()
        self.assertRegex(result, "[0-9]{26}")

    def test_get_account_details(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        result = bankAccount.getAccountDetails()
        self.assertRegex(result, "Numer konta: [0-9]{26}, Oddział: test_name -"
                                 " test_street test_houseNumber, test_zipCode test_city")

    def test_get_nip(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        seller_test = seller.Seller("test_firstname", "test_lastname", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "test_companyName")
        result = seller_test.getNip()
        self.assertRegex(result, "[0-9]{10}")

    def test_get_seller(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        seller_test = seller.Seller("test_firstname", "test_lastname", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "test_companyName")
        result = seller_test.getSeller()
        self.assertRegex(result, "Sprzedawca: \ntest_companyName - test_firstname test_lastname,"
                                 " test_street test_houseNumber, test_zipCode test_city, NIP: [0-9]{10},"
                                 " konto bankowe: Numer konta: [0-9]{26}, Oddział: test_name -"
                                 " test_street test_houseNumber, test_zipCode test_city")

    def test_get_product_value(self):
        test_product = product.Product("product_name", 10, 0.23, 1)
        result = test_product.getValue()
        self.assertEqual(result, 12.30)

    def test_get_price_for_invoice(self):
        test_product = product.Product("product_name", 10, 0.23, 1)
        result = test_product.getPriceForInvoice()
        self.assertEqual(result, "product_name: 1szt. cena jednostkowa netto: 10zł, cena netto: 10zł,"
                                 " VAT: 23.0%, wartość VAT: 2.3zł, cena brutto: 12.3zł")

    def test_price_lower_than_0(self):
        with self.assertRaises(exceptions.PriceLowerThanZeroError):
            product.Product("product_name", -10, 0.23, 1)

    def test_vat_higher_than_1(self):
        with self.assertRaises(exceptions.VatMustBeBetweenZeroAndOneError):
            product.Product("product_name", 10, 1.23, 1)

    def test_vat_lower_than_0(self):
        with self.assertRaises(exceptions.VatMustBeBetweenZeroAndOneError):
            product.Product("product_name", 10, -0.23, 1)

    def test_quantity_lower_than_0(self):
        with self.assertRaises(exceptions.QuantityLowerThanZeroError):
            product.Product("product_name", 10, 0.23, -1)

    def test_empty_products(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        test_customer = customer.Customer("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                          "test_zipCode", "test_city")
        test_seller = seller.Seller("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "Tomex")
        test_invoice = invoice.Invoice(test_customer, test_seller, "22-10-2021", "21-10-2021")
        result = test_invoice.getProducts()
        self.assertEqual(result, "")

    def test_add_product(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        test_customer = customer.Customer("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                          "test_zipCode", "test_city")
        test_seller = seller.Seller("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "Tomex")
        test_product = product.Product("product_name", 10, 0.23, 1)
        test_invoice = invoice.Invoice(test_customer, test_seller, "22-10-2021", "21-10-2021")
        test_invoice.addProduct(test_product)
        self.assertEqual(test_invoice.products, ["product_name: 1szt. cena jednostkowa netto: 10zł, cena netto: 10zł,"
                                                 " VAT: 23.0%, wartość VAT: 2.3zł, cena brutto: 12.3zł"])

    def test_added_products(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        test_customer = customer.Customer("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                          "test_zipCode", "test_city")
        test_seller = seller.Seller("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "Tomex")
        test_product = product.Product("product_name", 10, 0.23, 1)
        test_invoice = invoice.Invoice(test_customer, test_seller, "22-10-2021", "21-10-2021")
        test_invoice.addProduct(test_product)
        result = test_invoice.getProducts()
        self.assertEqual(result, "product_name: 1szt. cena jednostkowa netto: 10zł, cena netto: 10zł,"
                                 " VAT: 23.0%, wartość VAT: 2.3zł, cena brutto: 12.3zł\n")

    def test_get_invoice(self):
        bankAccount = bank.Bank("test_name", "test_street", "test_houseNumber", "test_zipCode", "test_city")
        test_customer = customer.Customer("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                          "test_zipCode", "test_city")
        test_seller = seller.Seller("test_firstName", "test_lastName", "test_street", "test_houseNumber",
                                    "test_zipCode", "test_city", bankAccount, "test_company_name")
        test_invoice = invoice.Invoice(test_customer, test_seller, "22-10-2021", "21-10-2021")
        result = test_invoice.getInvoice()
        self.assertRegex(result, f"Numer faktury: [0-9]*/{datetime.date.today().month}/{datetime.date.today().year} "
                                 "\nSprzedawca: \ntest_company_name - test_firstName test_lastName, "
                                 "test_street test_houseNumber, test_zipCode test_city, NIP: [0-9]{10}, "
                                 "konto bankowe: Numer konta: [0-9]{26}, Oddział: test_name - "
                                 "test_street test_houseNumber, test_zipCode test_city \nNabywca: \ntest_firstName "
                                 "test_lastName, test_street test_houseNumber, test_zipCode test_city \nProdukty: "
                                 "\nWartość całkowita: 0zł \nData sprzedaży: 2021-10-21 \nData zapłaty: 2021-10-22 "
                                 f"\nData wystawienia faktury: {datetime.date.today()}")


if __name__ == '__main__':
    unittest.main()
