__author__ = 'michaelluo'

import unittest
import getPrice

class TestPriceFunctions(unittest.TestCase):

    def test_tryGettingPrice(self):
        priceJSON = getPrice.tryGettingPrice(2)
        self.assertIsNotNone(priceJSON)
        self.assertTrue(priceJSON.has_key('subtotal'))
        self.assertTrue(priceJSON['subtotal'].has_key('amount'))

    def test_getCoinbasePrice(self):
        price = getPrice.getCoinbasePrice()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)
if __name__ == '__main__':
    unittest.main()