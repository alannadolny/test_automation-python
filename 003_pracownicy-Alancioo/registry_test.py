import unittest
import exceptions
import office_worker
import physical_worker
import registry
import seller
import worker


class RegistryTest(unittest.TestCase):
    def test_add_seller(self):
        company = worker.Company()
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "low", 20)
        test_registry = registry.Registry()
        test_registry.addWorker(test_seller)
        result = test_registry.getSortedWorkers()
        self.assertEqual(result, ["test_name test_lastName"])

    def test_add_physical_worker(self):
        company = worker.Company()
        test_physical_worker = physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street",
                                                              5, 6, "test_city", company, 99)
        test_registry = registry.Registry()
        test_registry.addWorker(test_physical_worker)
        result = test_registry.getSortedWorkers()
        self.assertEqual(result, ["test_name test_lastName"])

    def test_add_office_worker(self):
        company = worker.Company()
        test_office_worker = office_worker.OfficeWorker("test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                                        "test_city", company, 80)
        test_registry = registry.Registry()
        test_registry.addWorker(test_office_worker)
        result = test_registry.workers
        self.assertEqual(result, [test_office_worker])

    def test_add_inappropriate_worker(self):
        with self.assertRaises(exceptions.InappropriateWorkerType):
            test_registry = registry.Registry()
            test_registry.addWorker("inappropriate worker")

    def test_add_many_workers(self):
        company = worker.Company()
        test_office_worker = office_worker.OfficeWorker("first_test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                                        "test_city", company, 80)
        test_physical_worker = physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street",
                                                              5, 6, "test_city", company, 99)
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "low", 20)
        test_registry = registry.Registry()
        test_registry.addManyWorkers([test_office_worker, test_physical_worker, test_seller])
        result = test_registry.workers
        self.assertEqual(result, [test_office_worker, test_physical_worker, test_seller])

    def test_add_many_workers_with_inappropriate_type(self):
        with self.assertRaises(exceptions.InappropriateWorkerTypeInList):
            company = worker.Company()
            test_office_worker = office_worker.OfficeWorker("first_test_name", "test_lastName", 45, 12, "test_street",
                                                            7, 4, "test_city", company, 80)
            test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                        "low", 20)
            test_registry = registry.Registry()
            test_registry.addManyWorkers([test_office_worker, "inappropriate_worker", test_seller])

    def test_delete_worker(self):
        company = worker.Company()
        first_office_worker = office_worker.OfficeWorker("first_test_name", "test_lastName", 45, 12, "test_street", 7,
                                                         4,
                                                         "test_city", company, 80)
        second_office_worker = office_worker.OfficeWorker("second_test_name", "test_lastName", 45, 12, "test_street", 7,
                                                          4,
                                                          "test_city", company, 80)
        test_registry = registry.Registry()
        test_registry.addManyWorkers([first_office_worker, second_office_worker])
        test_registry.deleteWorker(first_office_worker.workerId)
        result = test_registry.workers
        self.assertEqual(result, [second_office_worker])

    def test_get_empty_workers(self):
        test_registry = registry.Registry()
        result = test_registry.getSortedWorkers()
        self.assertEqual(result, "Lack of employees")

    def test_get_sorted_workers(self):
        company = worker.Company()
        first_office_worker = office_worker.OfficeWorker("first_test_name", "atest_lastName", 45, 12, "test_street", 7,
                                                         4,
                                                         "test_city", company, 80)
        second_office_worker = office_worker.OfficeWorker("second_test_name", "test_lastName", 45, 12, "test_street", 7,
                                                          4,
                                                          "test_city", company, 80)
        third_office_worker = office_worker.OfficeWorker("third_test_name", "test_lastName", 47, 12, "test_street", 7,
                                                         4,
                                                         "test_city", company, 80)
        fourth_office_worker = office_worker.OfficeWorker("fourth_test_name", "test_lastName", 45, 8, "test_street", 7,
                                                          4,
                                                          "test_city", company, 80)
        test_registry = registry.Registry()
        test_registry.addManyWorkers(
            [first_office_worker, second_office_worker, third_office_worker, fourth_office_worker])
        result = test_registry.getSortedWorkers()
        self.assertEqual(result, ["first_test_name atest_lastName", "second_test_name test_lastName",
                                  "third_test_name test_lastName", "fourth_test_name test_lastName"])

    def test_empty_workers_by_city(self):
        test_registry = registry.Registry()
        result = test_registry.getWorkersByCity("test city")
        self.assertEqual(result, "No employee works in this city")

    def test_get_workers_by_city(self):
        company = worker.Company()
        first_office_worker = office_worker.OfficeWorker("first_test_name", "atest_lastName", 45, 12, "test_street", 7,
                                                         4,
                                                         "test_city", company, 80)
        second_office_worker = office_worker.OfficeWorker("second_test_name", "test_lastName", 45, 12, "test_street", 7,
                                                          4,
                                                          "test_city2", company, 80)
        test_registry = registry.Registry()
        test_registry.addManyWorkers([first_office_worker, second_office_worker])
        result = test_registry.getWorkersByCity("test_city")
        self.assertEqual(result, ["first_test_name atest_lastName"])

    def test_get_workers_with_their_values(self):
        company = worker.Company()
        test_office_worker = office_worker.OfficeWorker("first_test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                                        "test_city", company, 80)
        test_physical_worker = physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street",
                                                              5, 6, "test_city", company, 99)
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "low", 20)
        test_registry = registry.Registry()
        test_registry.addManyWorkers([test_office_worker, test_physical_worker, test_seller])
        result = test_registry.getWorkersWithValue()
        self.assertEqual(result, ["first_test_name test_lastName, value: 960", "test_name test_lastName, value: 24.75",
                                  "test_name test_lastName, value: 900"])


if __name__ == '__main__':
    unittest.main()
