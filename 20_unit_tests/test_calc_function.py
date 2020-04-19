import unittest
import calc_function
import math

'''

1. import the function that you need e.g. import unittest
2. create a test case Class in the test file
3. define the test case (which is a method) - the test case is written in the method
4. the test case name (method) must begin with "test_"
'''
class test_calc_function(unittest.TestCase):

    def test_calc_add(self):
        #result = calc_function.add(10, 5)
        self.assertEqual(calc_function.add(10, 5), 15)
        print("1")
        self.assertEqual(calc_function.add(-1, -2), -3)
        print("2")
        self.assertEqual(calc_function.add(1, 2), 3)
        print("3")

    def test_calc_subtract(self):
        result = calc_function.subtract(10, 2)
        self.assertEqual(result, 8)
        print("4")

    def test_calc_multiply(self):
        result = calc_function.multiply(3, 15)
        self.assertEqual(result, 45)
        print("5")


if __name__ == '__main__':
    unittest.main()



