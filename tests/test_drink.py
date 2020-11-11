import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Bourbon", 5)

    #@unittest.skip("Delete this line to run the test")
    def test_drink_has_name(self):
        self.assertEqual("Bourbon", self.drink    .name)

    #@unittest.skip("Delete this line to run the test")
    def test_drink_price(self):
        self.assertEqual(5, self.drink.price)




    # remove drink from pub stock
    
    # give drink to customer 