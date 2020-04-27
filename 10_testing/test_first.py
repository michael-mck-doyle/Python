import unittest

import first


class TestUnit(unittest.TestCase):
    """docstring placeholder"""

    @classmethod
    def setUpClass(cls):
        print('Class level hook method for setting up class fixture before running tests in the class.')

    @classmethod
    def tearDownClass(cls):
        print("Class level hook method for deconstructing the class fixture after running all tests in the class.")

    def setUp(self):
        print("Test level hook method for setting up the test fixture before each individual test.")

    def tearDown(self):
        print("Test level hook method for deconstructing the test fixture after each individual test.")
        pass

    def test_add(self):
        self.assertEqual(first.addition(9, 8), 17)

    def test_greater(self):
        self.assertGreater(first.greater(9, 8), 5)

    def test_subtract(self):
        self.assertEqual(first.subtraction(9, 8), 1+7)

    def test_is_not_add(self):
        self.assertIsNot(first.is_not(5, 5), 10)


if __name__ == '__main__':
    unittest.main()

