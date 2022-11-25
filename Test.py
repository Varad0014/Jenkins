#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int1(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 50)
    def test_list_int2(self):
        """
        Test case to add two numbers
        """
        data = [40, 30]
        result = summation(data)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
