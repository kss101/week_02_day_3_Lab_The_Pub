import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Moe’s Tavern", 500)
        self.drink = Drink("Bourbon", 5)

    #@unittest.skip(“Delete this line to run the test”)
    def test_pub_has_name(self):
        self.assertEqual("Moe’s Tavern", self.pub.name)
    #unittest.skip(“Delete this line to run the test”)
    def test_pub_till_total(self):
        self.assertEqual(500, self.pub.till)

    def test_add_drink_to_stock(self):
        self.pub.add_drink_to_stock(self.drink)
        self.assertEqual(1, self.pub.stock_check())
