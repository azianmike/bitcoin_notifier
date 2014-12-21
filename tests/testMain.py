__author__ = 'michaelluo'

import unittest
import main

class TestSequenceFunctions(unittest.TestCase):

    def test_checkArgs(self):
        self.assertTrue(main.checkValidArgs([1,2]))
        self.assertFalse(main.checkValidArgs(['.py', '340.00', '>=', 'test@test.com', '1']))
        self.assertFalse(main.checkValidArgs(['.py', '340', '>=', 'test@test.com', '1']))
        self.assertTrue(main.checkValidArgs(['.py', '340', 'blah', 'test@test.com', '1']))

if __name__ == '__main__':
    unittest.main()