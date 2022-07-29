import unittest
from unittest.mock import Mock, MagicMock, call
import exceptions
from Storehouse import Storehouse
from InvoiceRepository import InvoiceRepository
from Shop import Shop
from Invoice import Invoice


def adding_product_with_inappropriate_data(product):
    if 'name' in product and 'quantity' in product:
        return product
    else:
        return exceptions.InvalidProductData


class ShopTests(unittest.TestCase):
    def test_buy_product_which_is_not_in_storehouse(self):
        dummy_repository = Mock(InvoiceRepository)
        stub_storehouse = MagicMock(Storehouse)
        stub_storehouse.getFromStorehouse = MagicMock(side_effect=exceptions.OutOfStore)
        shop = Shop(dummy_repository, stub_storehouse)
        with self.assertRaises(exceptions.OutOfStore):
            shop.buy(customer='Jan', items_list=['czekolada'])

    def test_add_product_with_inappropriate_data_to_storehouse(self):
        fake_storehouse = Mock(Storehouse)
        fake_storehouse.addToStorehouse = MagicMock(side_effect=adding_product_with_inappropriate_data(product={'inappropriate_name': 'czekolada', 'quantity': 1}))
        with self.assertRaises(exceptions.InvalidProductData):
            fake_storehouse.addToStorehouse()

    def test_buy_last_valid_product_which_is_in_storehouse(self):
        dummy_repository = Mock(InvoiceRepository)
        storehouse = Storehouse([{'name': 'czekolada', 'quantity': 1}])
        shop = Shop(dummy_repository, storehouse)
        shop.buy(customer='Jan', items_list=['czekolada'])
        self.assertEqual(storehouse.productsList, [])

    def test_buy_product_which_has_higher_quantity(self):
        dummy_repository = Mock(InvoiceRepository)
        storehouse = Storehouse([{'name': 'czekolada', 'quantity': 2}])
        shop = Shop(dummy_repository, storehouse)
        shop.buy(customer='Jan', items_list=['czekolada'])
        self.assertEqual(storehouse.productsList, [{'name': 'czekolada', 'quantity': 1}])

    def test_returning_all_goods_called_repository_once(self):
        spy_repository = Mock(InvoiceRepository)
        spy_storehouse = Mock(Storehouse)
        shop = Shop(spy_repository, spy_storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada']))
        spy_repository.delete.assert_called_once()

    def test_returning_one_good_called_storehouse_once(self):
        spy_repository = Mock(InvoiceRepository)
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(spy_repository, dummy_storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada']))
        dummy_storehouse.addToStorehouse.assert_called_once()

    def test_returning_all_goods_called_multiple_times(self):
        spy_repository = Mock(InvoiceRepository)
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(spy_repository, dummy_storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko']))
        dummy_storehouse.addToStorehouse.assert_has_calls(
            [call({'name': 'Czekolada', 'quantity': 1}), call({'name': 'Ciastko', 'quantity': 1})], any_order=False)

    def test_partial_returning_once_called_update(self):
        spy_repository = Mock(InvoiceRepository)
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(spy_repository, dummy_storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko']),
                             partial_returning=['Czekolada'])
        spy_repository.update.assert_called_once()

    def test_partial_returning_goods_to_storehouse_called_multiple_times(self):
        spy_repository = Mock(InvoiceRepository)
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(spy_repository, dummy_storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko', 'Drożdżówka']),
                             partial_returning=['Czekolada', 'Ciastko'])
        dummy_storehouse.addToStorehouse.assert_has_calls(
            [call({'name': 'Czekolada', 'quantity': 1}), call({'name': 'Ciastko', 'quantity': 1})], any_order=False)

    def test_partial_returning_goods_correctly_add_items_to_storehouse(self):
        spy_repository = Mock(InvoiceRepository)
        storehouse = Storehouse()
        shop = Shop(spy_repository, storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko', 'Drożdżówka']),
                             partial_returning=['Czekolada', 'Ciastko'])
        self.assertEqual(storehouse.productsList,
                         [{'name': 'Czekolada', 'quantity': 1}, {'name': 'Ciastko', 'quantity': 1}])

    def test_returning_all_goods_from_invoice_to_storehouse(self):
        spy_repository = Mock(InvoiceRepository)
        storehouse = Storehouse([])
        shop = Shop(spy_repository, storehouse)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko', 'Drożdżówka']))
        self.assertEqual(storehouse.productsList,
                         [{'name': 'Czekolada', 'quantity': 1}, {'name': 'Ciastko', 'quantity': 1},
                          {'name': 'Drożdżówka', 'quantity': 1}])

    def test_if_shop_properly_add_invoices_to_repository(self):
        repository = InvoiceRepository()
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(repository, dummy_storehouse)
        shop.buy(customer='Jan', items_list=['Czekolada', 'Ciastko'])
        self.assertEqual(repository.data_source, [Invoice(1, 'Jan', ['Czekolada', 'Ciastko'])])

    def test_if_shop_properly_delete_invoices_from_repository(self):
        repository = InvoiceRepository()
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(repository, dummy_storehouse)
        shop.returning_goods(invoice=Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko']))
        self.assertEqual(repository.data_source, [])

    def test_if_shop_properly_update_invoices_in_repository(self):
        repository = InvoiceRepository()
        dummy_storehouse = Mock(Storehouse)
        shop = Shop(repository, dummy_storehouse)
        shop.buy(customer='Jan', items_list=['Czekolada', 'Ciastko'])
        shop.returning_goods(invoice=Invoice(number=1, customer='Jan', items=['Czekolada', 'Ciastko']),
                             partial_returning=['Czekolada'])
        self.assertEqual(repository.data_source, [Invoice(2, 'Jan', ['Ciastko'])])
