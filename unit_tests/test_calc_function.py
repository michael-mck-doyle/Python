'''
1. import the function that you need e.g. import unittest
2. create a test case Class in the test file
3. define the test case (which is a method) - the test case is written in the method
4. the test case name (method) must begin with "test_"
'''


import unittest
from unit_tests import calc_Function


class test_calc_function(unittest.TestCase):

    def test_calc_add(self):
        #result = calc_function.add(10, 5)
        self.assertEqual(calc_Function.add(10, 5), 15)
        print("1")
        self.assertEqual(calc_Function.add(-1, -2), -3)
        print("2")
        self.assertEqual(calc_Function.add(1, 2), 3)
        print("3")

    def test_calc_subtract(self):
        result = calc_Function.subtract(10, 2)
        self.assertEqual(result, 8)
        print("4")

    def test_calc_multiply(self):
        result = calc_Function.multiply(3, 15)
        self.assertEqual(result, 45)
        print("5")

    def test_calc_divide(self):
        #result = calc_function.divide()
        self.assertEqual(calc_Function.divide(9, 3))
        with self.assertRaises(ValueError):
            calc_Function


if __name__ == '__main__':
    unittest.main()




