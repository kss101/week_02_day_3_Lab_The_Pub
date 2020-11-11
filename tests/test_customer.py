import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Meatloaf", 100)

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("Meatloaf", self.customer.name)

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_cash(self):
        self.assertEqual(100, self.customer.wallet)

    # # Purchase item (booze, food)
    # def test_customer_buy_item(self):
    #     item = Drink("Bourbon", 5)



    #     self.assertEqual("Bourbon", self.customer.buy_item(item))
    #     # self.assertEqual(95, self.customer.wallet)


    # Reduce money in wallet by prince of item

    # Send money from wallet to till


