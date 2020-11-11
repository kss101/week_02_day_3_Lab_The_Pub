import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub(“Mo’s Tavern”, 500,)
    #@unittest.skip(“Delete this line to run the test”)
    def test_pub_has_name(self):
        self.assertEqual(“Mo’s Tavern”, self.pub.name)
    #unittest.skip(“Delete this line to run the test”)
    def test_pub_till_total(self):
        self.assertEqual(500, self.pub.till)