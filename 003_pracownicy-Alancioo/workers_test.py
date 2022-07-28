import unittest
import address
import exceptions
import worker
import office_worker
import physical_worker
import seller


class WorkersTest(unittest.TestCase):
    def test_generate_id(self):
        company = worker.Company()
        generated_id = company.generateId()
        self.assertRegex(str(generated_id), "[0-9]*")

    def test_generating_office_identifier(self):
        company = worker.Company()
        generated_office_identifier = company.generatingOfficeIdentifier()
        self.assertRegex(str(generated_office_identifier), "[0-9]*")

    def test_inappropriate_effectiveness(self):
        with self.assertRaises(exceptions.EffectivenessMustBeLowOrMidOrHigh):
            company = worker.Company()
            seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                          "bad_effectiveness", 20)

    def test_low_effectiveness(self):
        company = worker.Company()
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "low", 20)
        self.assertEqual(test_seller.effectiveness, "low")

    def test_mid_effectiveness(self):
        company = worker.Company()
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "mid", 20)
        self.assertEqual(test_seller.effectiveness, "mid")

    def test_high_effectiveness(self):
        company = worker.Company()
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "high", 20)
        self.assertEqual(test_seller.effectiveness, "high")

    def test_setting_provision(self):
        company = worker.Company()
        test_seller = seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                                    "high", 20)
        self.assertEqual(test_seller.provision, 20)

    def test_provision_lower_than_0(self):
        with self.assertRaises(exceptions.ProvisionMustBeBetween0And100):
            company = worker.Company()
            seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                          "high", -20)

    def test_provision_higher_than_0(self):
        with self.assertRaises(exceptions.ProvisionMustBeBetween0And100):
            company = worker.Company()
            seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                          "high", 120)

    def test_provision_is_a_string(self):
        with self.assertRaises(exceptions.ProvisionMustBeANumber):
            company = worker.Company()
            seller.Seller("test_name", "test_lastName", 20, 15, "test_street", 5, 6, "test_city", company,
                          "high", "provision")

    def test_setting_strength(self):
        company = worker.Company()
        test_physical_worker = physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street", 5, 6,
                                                              "test_city", company, 60)
        self.assertEqual(test_physical_worker.strength, 60)

    def test_strength_lower_than_0(self):
        with self.assertRaises(exceptions.StrengthMustBeBetween1And100):
            company = worker.Company()
            physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street",
                                           5, 6, "test_city", company, -60)

    def test_strength_higher_than_100(self):
        with self.assertRaises(exceptions.StrengthMustBeBetween1And100):
            company = worker.Company()
            physical_worker.PhysicalWorker("test_name", "test_lastName", 40, 10, "test_street",
                                           5, 6, "test_city", company, 101)

    def test_setting_iq(self):
        company = worker.Company()
        test_office_worker = office_worker.OfficeWorker("test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                                        "test_city", company, 80)
        self.assertEqual(test_office_worker.iq, 80)

    def test_iq_lower_than_70(self):
        with self.assertRaises(exceptions.IqMustBeBetween70And150):
            company = worker.Company()
            office_worker.OfficeWorker("test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                       "test_city", company, 65)

    def test_iq_higher_than_150(self):
        with self.assertRaises(exceptions.IqMustBeBetween70And150):
            company = worker.Company()
            office_worker.OfficeWorker("test_name", "test_lastName", 45, 12, "test_street", 7, 4,
                                       "test_city", company, 162)

    def test_get_address(self):
        test_address = address.Address("test_street", 4, 3, "test_city")
        result = test_address.getAddress()
        self.assertEqual(result, 'address: test_city, test_street 4/3')


if __name__ == '__main__':
    unittest.main()
