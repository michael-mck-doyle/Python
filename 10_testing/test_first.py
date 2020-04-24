import unittest

import first


class TestUnit(unittest.TestCase):
    """docstring placeholder"""
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

