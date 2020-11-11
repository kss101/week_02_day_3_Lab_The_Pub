import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Meatloaf", 100)

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("Meatloaf", self.customer.name)

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_cash(self):
        self.assertEqual(100, self.customer.wallet)