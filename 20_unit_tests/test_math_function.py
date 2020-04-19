import unittest
import math_function

class KnownValue(unittest.TestCase):
    def test_areaCircle_for_10_radius(self):
        # capture the results of the function
        result = math_function.areaCircle(self)
        # check for expected output
        expected = 314
        self.assertEqual(expected, result)
    def test_areaCircle_for_2_radius(self):
        # capture the results of the function
        result = math_function.areaCircle(self)
        # check for expected output
        expected = 4
        self.assertEqual(expected, result)
    def test_areaCircle_for_5_radius(self):
        # capture the results of the function
        result = math_function.areaCircle(self)
        # check for expected output
        #r = int(input("Enter radius of cirlce"))
        expected = 314
        self.assertEqual(expected, result)


    # Run the tests

    if __name__ == '__main__':
        unittest.main()
